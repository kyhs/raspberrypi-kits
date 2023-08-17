
import RPi.GPIO as GPIO
import time
import sys
import os
import requests
import json

GPIO4 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
LastStatus = False

API_HOST = 'https://api.switch-bot.com'
TOKEN = os.getenv('TOKEN')
DEVICE_ID = os.getenv('DEVICE_ID')


def execute_switchbot_api():
    url = f"{API_HOST}/v1.0/devices/{DEVICE_ID}/commands"
    headers = {
        'Authorization': TOKEN,
        'Content-Type': 'application/json'
    }
    command = {
        "command": "turnOn"
    }
    res = requests.post(url, data=json.dumps(command), headers=headers)
    return  res.json()

while True:
    try:
        SwitchStatus = GPIO.input(GPIO4)
        if LastStatus != SwitchStatus:
            if SwitchStatus == 1:
                print("pushed")
                result = execute_switchbot_api()
                print(result)
            time.sleep(0.2)
        LastStatus = SwitchStatus
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()