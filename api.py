from flask import Flask, request, jsonify
import numpy as np
import pickle
import joblib


#### THIS IS WHAT WE DO IN POSTMAN ###
# STEP 1: Create New Request
# STEP 2: Select POST
# STEP 3: Type correct URL (http://127.0.0.1:5000/prediction)
# STEP 4: Select Body
# STEP 5: Select raw and then JSON type
# STEP 6: Type or Paste in example json request
# STEP 7: Run 01-Basic-API.py to launch server and confirm the site is running
# Step 8: Run API request

### IMP NOTES
# Set localhost = '0.0.0.0' and port = 8080 in 01-Basic-API.py
# To accept the request from other client over a wifi Connection

def final_prediction(model, scaler, data):
    c = list(data.values())
    e = np.array(c, dtype=int)
    w = scaler.transform([e])
    res = model.predict(w)
    label = ["Insomnia", "None", "Sleep Apnea", ]
    return label[res[0]]

# REMEMBER TO LOAD THE MODEL AND THE SCALER!

# LOAD THE SVC MODEL
m= joblib.load("models/RFC.pkl")
s= joblib.load("models/scaler.pkl")

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNINGjhgjhSK!</h1>'

@app.route('/prediction', methods=['POST'])
def predict_disorder(scaler=None):
    # RECIEVE THE REQUEST
    content = request.json

    # PRINT THE DATA PRESENT IN THE REQUEST
    print("[INFO] Request: ", content)

    # PREDICT THE CLASS USING HELPER FUNCTION
    results = final_prediction(model=m,
                                scaler=s,
                                data=content)

    # PRINT THE RESULT
    print("[INFO] Responce: ", results)

    # SEND THE RESULT AS JSON OBJECT
    return jsonify(results)


if __name__ == '__main__':
    app.run("0.0.0.0")
