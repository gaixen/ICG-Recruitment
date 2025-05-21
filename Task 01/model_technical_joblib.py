import joblib
#since model_rf is the best model
joblib.dump(model_rf, 'model_technicals/model.joblib') 
joblib.dump(scaler, 'model_technicals/scaler.joblib')
joblib.dump(pt, 'model_technicals/powertransformer.joblib')
joblib.dump(le, 'model_technicals/labelencoder.joblib')
joblib.dump(selected_features_name, 'model_technicals/features.joblib')
