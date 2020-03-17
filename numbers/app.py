from flask import Flask, request, jsonify, Response
import requests
import random
app = Flask(__name__)

@app.route('/get')
def get(): 
    return [random.choice(range(10)) for i in range(3)]

if __name__ == '__main__':
    app.run(port=5002, host='0.0.0.0')