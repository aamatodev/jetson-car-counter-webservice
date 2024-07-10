import json

import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    url = 'http://10.100.4.58:5000/get-current-car-counter'

    x = requests.get(url).json()

    return jsonify(x)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
