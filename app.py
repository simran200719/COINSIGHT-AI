import joblib

from flask import Flask,render_template,request



app=Flask(__name__)

model=joblib.load('crypto.pkl')
scaler=joblib.load('scaler.pkl')

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

    prediction=model.predict([[Open,High,Low,Close,Volume]])
    return render_template('index.html',result=prediction[0])
    
if __name__=='__main__':
    app.run(debug=True)
