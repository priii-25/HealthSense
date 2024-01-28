import json
import requests
url = 'http://127.0.0.1:5500//heartDisease'
input_data_for_model = {
    'age':59;
    'sex':1;
    'cp':1;
    'trestbps':140;
    'chol':221;
    'fbs':0;
    'restecg':1;
    'thalach':164;
    'exang':1;
    'oldpeak':0.0;
    'slope':2;
    'ca':0;
    'thal':2;
    }
input_json = json.dumps(input_data_for_model)
response = requests.post(url, data=input_json)
print(response.text)