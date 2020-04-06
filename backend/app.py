from flask import Flask, request, jsonify, Response
import requests
from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

@app.route('/')
@app.route('/roll', methods=['GET','POST'])
def roll():
    nums = requests.get("http://numbers:5003/get")
    letts = requests.get("http://letters:5002/get")
    return str(letts.text)+str(nums.text)

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')