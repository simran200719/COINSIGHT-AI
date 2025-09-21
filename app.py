import joblib
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request



app=Flask(__name__)
scaler=joblib.load('scaler.pkl')
model=joblib.load('crypto.pkl')
scaler_y=joblib.load('scaler_y.pkl')

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

    user_input=np.array([[Open,High,Low,Close,Volume]])
    scaled_input=scaler.transform(user_input)
    prediction=model.predict(scaled_input)
    predict=scaler_y.inverse_transform(prediction.reshape(-1,1))
    return render_template('index.html',result=predict[0][0])
    
if __name__=='__main__':
    app.run(debug=True)
