import joblib
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request
import numpy as np


app=Flask(__name__)

model=joblib.load('crypto.pkl')
scaler_x_full=joblib.load('scaler_x_full.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def pred():
    Open=float(request.form.get('open'))
    High=float(request.form.get('high'))
    Low=float(request.form.get('low'))
    Close=float(request.form.get('close'))
    Volume=float(request.form.get('volume'))

    user_input=[[Open,High,Low,Close,Volume]]
    scaled_input=scaler_x_full.transform(user_input)
    prediction=model.predict(scaled_input)
    
    return render_template('index.html',result=prediction[0][0])
    
if __name__=='__main__':
    app.run(debug=True)
