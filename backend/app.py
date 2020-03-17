from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

@app.route('/')

@app.route('/get/num')
def getnum():
    return numgen()

@app.route('/get/char')
def getchar():
    return requests.get('https://letters:5001/get').json()

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')