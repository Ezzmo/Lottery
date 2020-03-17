from numbergen import numgen
from letters.lettergen import letgen
import requests

@app.route('/')

@app.route('/get/num')
def getnum():
    return numgen()

@app.route('/get/char')
def getchar():
    return requests.get('https://letters:5001/get').json()

