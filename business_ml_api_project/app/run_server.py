import logging
from logging.handlers import RotatingFileHandler
import os
import pickle   # Or can use joblib
import time

import pandas as pd

import flask


def load_model(model_path):
    
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    return model


# Logging
logfile = 'model_api.log'
handler = RotatingFileHandler(filename=logfile, maxBytes=1048576, backupCount=5)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Initialize Flask app
app = flask.Flask(__name__)

# Load the model
model_file = 'app/models/model.pkl'
model = load_model(model_file)


@app.route('/', methods=['GET'])
def general():
    return """Welcome to Airline Passenger Satisfaction prediction API!"""


@app.route('/predict', methods=['POST'])
def predict():
    # initialize the data dictionary that will be returned from the view
    response = {'success': False}
    curr_time = time.strftime('[%Y-%b-%d %H:%M:%S]')
    
    if flask.request.method == 'POST':
        request_json = flask.request.get_json()
        
        input_data = pd.DataFrame({
            'Inflight wifi service': request_json.get('Inflight wifi service', ''),
            'Type of Travel': request_json.get('Type of Travel', ''),
            'Customer Type': request_json.get('Customer Type', ''),
            'Baggage handling': request_json.get('Baggage handling', ''),
            'Online boarding': request_json.get('Online boarding', ''),
            'Class': request_json.get('Class', ''),
            'Inflight service': request_json.get('Inflight service', ''),
            'Checkin service': request_json.get('Checkin service', ''),
            'Gate location': request_json.get('Gate location', ''),
            'Seat comfort': request_json.get('Seat comfort', ''),
            'Age': request_json.get('Age', ''),
            'Cleanliness': request_json.get('Cleanliness', '')
        }, index=[0])
        logger.info(f'{curr_time} Data: {input_data.to_dict()}')
        
        try:
            # Predict the result
            preds = model.predict_proba(input_data)
            response['predictions'] = round(preds[:, 1][0], 5)
            # Request successful
            response['success'] = True
        except AttributeError as e:
            logger.warning(f'{curr_time} Exception: {str(e)}')
            response['predictions'] = str(e)
            # Request unsuccessful
            response['success'] = False
    
    # return the data dictionary as a JSON response
    return flask.jsonify(response)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    port = int(os.environ.get('FLASK_SERVER_PORT', 8180))
    app.run(host='0.0.0.0', debug=True, port=port)