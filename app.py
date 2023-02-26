from flask import Flask
import requests
import os

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
 
@app.route('/')
def get_forecast():
    city = "Ho Chi Minh City"

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city,API_KEY)
    print(url)
    res = requests.get(url)
    data = res.json()

    return data

@app.route('/readiness')
def readiness():
    return "Success"

@app.route('/liveness')
def liveness():
    return "Success"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
