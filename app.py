import joblib
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request
import numpy as np
import requests


app=Flask(__name__)

model=joblib.load('crypto.pkl')
scaler_x=joblib.load('scaler_x.pkl')

@app.route('/')
def home():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd', timeout=5) #fetched using  API
        response.raise_for_status()  # This will raise an HTTPError if status != 200
        data = response.json()
        btc_price = data['bitcoin']['usd']
    except Exception as e:
        print("Error fetching price:", e)  # This prints error to console
        btc_price = "Error fetching price"
    
    return render_template('home.html', btc_price=btc_price)


    
@app.route('/start')
def startt():
    return render_template('index.html')
    
@app.route('/predict',methods=['POST','GET'])
def pred():
    Open=float(request.form.get('open'))
    High=float(request.form.get('high'))
    Low=float(request.form.get('low'))
    Close=float(request.form.get('close'))
    Volume=float(request.form.get('volume'))

    user_input=[[Open,High,Low,Close,Volume]]
    scaled_input=scaler_x.transform(user_input)
    prediction=model.predict(scaled_input)
    
    return render_template('index.html',result=prediction[0])
    
if __name__=='__main__':
    app.run(debug=True)
