from fastapi import FastAPI
import json
import pickle
from pydantic import BaseModel

app = FastAPI()
class model_input(BaseModel):
    age : int
    sex : int
    cp : int
    trestbps : int
    chol: int
    fbs : int
    restecg : int
    thalach : int     
    exang : int
    oldpeak : float
    slope : int
    ca : int
    thal: int    
        
heartDisease_model = pickle.load(open('heart_disease.sav', 'rb'))

@app.post('/heartDisease')
def heartDiseasePred(input_parameters : model_input):
    
    inputD = input_parameters.json()
    inputDict = json.loads(inputD)
    
    a = inputDict['age']
    s = inputDict['sex']
    cp = inputDict['cp']
    st = inputDict['trestbps']
    ch= inputDict['chol']
    fbs = inputDict['fbs']
    r = inputDict['restecg']
    tlch = inputDict['thalach']
    e = inputDict['exang']
    op = inputDict['oldpeak']
    sl = inputDict['slope']
    ca = inputDict['ca']
    t = inputDict['thal']
    
    display = [a,s,cp,st,ch,fbs,r,tlch,e,op,sl,ca,t]
    prediction = heartDisease_model.predict([display])
    if (prediction[0] == 0):
        print('The person is likely to be free from heart disease')
    else:
        print('The person has a possibility of heart disease')