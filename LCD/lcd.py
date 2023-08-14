#!/usr/bin/env python3

import sys
sys.path.append('../lib')

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
import DHT

DHTPin = 11
 
def loop():
    mcp.output(3,1)
    lcd.begin(16,2)
    dht = DHT.DHT(DHTPin)
    while(True):
        # lcd.clear()
        lcd.setCursor(0,0)
        for i in range(0,15):
            chk = dht.readDHT11()
            if (chk is dht.DHTLIB_OK):
                print("OK")
                break
            sleep(0.1)
        lcd.message( 'T:' + str(dht.temperature) + ' M:' + str(dht.humidity) + '\n' )
        lcd.message( datetime.now().strftime('    %H:%M:%S') )   # display the time
        sleep(1)
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

