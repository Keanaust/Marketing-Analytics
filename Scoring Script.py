import json
import joblib
import numpy as np
import os

def init():
    global model
    # Load the trained model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')  # Ensure the model is saved as 'model.pkl'
    model = joblib.load(model_path)

def run(raw_data):
    try:
        # Parse the input data
        data = np.array(json.loads(raw_data)['data'])
        
        # Make predictions
        predictions = model.predict(data)
        probabilities = model.predict_proba(data)
        
        # Return predictions and probabilities
        return json.dumps({"predictions": predictions.tolist(), "probabilities": probabilities.tolist()})
    except Exception as e:
        return json.dumps({"error": str(e)})
