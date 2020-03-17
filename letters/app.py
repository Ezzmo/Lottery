from flask import Flask, request, jsonify, Response
import requests
import random
app = Flask(__name__)

@app.route('/get')
def get():
    letterz = "abcdefghijklmnopqrstuvwxyz"
    return [random.choice(letterz) for i in range(3)]

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')