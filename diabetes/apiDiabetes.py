from fastapi import FastAPI
import json
import pickle
from pydantic import BaseModel

app = FastAPI()
class model_input(BaseModel):
    
    pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int       
        
# loading the saved model
diabetes_model = pickle.load(open('diabetes_model (1).sav', 'rb'))

@app.post('/diabetes')
def diabetes_predd(input_parameters : model_input):
    
    inputD = input_parameters.json()
    inputDict = json.loads(inputD)
    
    p = inputDict['pregnancies']
    g = inputDict['Glucose']
    bp = inputDict['BloodPressure']
    st = inputDict['SkinThickness']
    i= inputDict['Insulin']
    bmi = inputDict['BMI']
    func = inputDict['DiabetesPedigreeFunction']
    a = inputDict['Age']
    
    display = [p, g, bp, st, i, bmi, func, a]
    prediction = diabetes_model.predict([display])
    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'