import joblib
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request


scaler=StandardScaler()
app=Flask(__name__)

model=joblib.load('crypto.pkl')
scaler=joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def pred():
    Open=float(scaler.fit_tranform(request.form.get('open')))
    High=float(scaler.fit_transform(request.form.get('high')))
    Low=float(scaler.fit_transform(request.form.get('low')))
    Close=float(sclaer.fit_transform(request.form.get('close')))	
    Volume=float(scaler.fit_transform(request.form.get('volume')))

    prediction=model.predict('open','high','low','close','volume')
    return render_template('index.html',result=prediction)
    
if __name__=='__main__':
    app.run(debug=True)
