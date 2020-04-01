from flask import Flask, request, jsonify, Response
import requests
import random
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

@app.route('/get', methods=['POST','GET'])
def get(): 
    roll = str([random.choice(range(1,51)) for i in range(3)]).strip("[]")
    return roll
if __name__ == '__main__':
    app.run(port=5003, host='0.0.0.0')