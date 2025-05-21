from flask import Flask, render_template, request
import numpy as np
import joblib
import pandas as pd
app = Flask(__name__)
#loading dumped model and preprocessing tools
model = joblib.load('model_technicals/model.joblib')
scaler = joblib.load('model_technicals/scaler.joblib')
pt = joblib.load('model_technicals/powertransformer.joblib')
le = joblib.load('model_technicals/labelencoder.joblib')
selected_features_name = joblib.load('model_technicals/features.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form[f'F{i}']) for i in range(1, 29)]
    df = pd.DataFrame([features], columns=[f'F{i}' for i in range(1, 29)])
    transformed = pt.transform(df)
    selected_df = pd.DataFrame(transformed, columns=df.columns)[selected_features_name]
    scaled = scaler.transform(selected_df)    
    prediction = model.predict(scaled)
    result = le.inverse_transform(prediction)[0]
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
