# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:37:29 2021

@author: arafa
"""

import flask, json, pickle
from flask import Flask, jsonify, request
from data_in_test import data_in
import numpy as np
from json import JSONEncoder

app = Flask(__name__)

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def load_models():
    file_name = '../models/model_file.p'
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


@app.route('/predict', methods=['GET'])

def predict():
    # stub input features
    request_json = request.get_json()
    x = request_json['input']
    print(x)
    x_in = np.array(x).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x_in)
    
    response = json.dumps({'response': prediction}, cls = NumpyArrayEncoder)
    return response, 200


if __name__ == '__main__':
    application.run(debug=True)
    
    
