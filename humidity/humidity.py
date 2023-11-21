#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT
from flask import Flask
from flask import jsonify

DHTPin = 11

app = Flask(__name__)

@app.route("/humidity")
def get_humidity():
    dht = DHT.DHT(DHTPin)
    chk = dht.readDHT11()
    if (chk is dht.DHTLIB_OK):
        res = {
            'temperature': dht.temperature,
            'humidity': dht.humidity
        }
    else:
        res = {
            'temperature': 'error',
            'humidity': 'error'
        }
    return jsonify(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
