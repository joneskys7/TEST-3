import RPi.GPIO as GPIO
import time
import spidev
from time import sleep
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

spi = spidev.SpiDev()
spi.open(0,0)

count=0
gas_channel = 0
temp_channel = 1

def getReading(channel):
    rawData = spi.xfer([1,(8 + channel)<<4,0])
    processedData = ((rawData[1]&3)<<8)+rawData[2]
    return processedData
while True:
    data = getReading(gas_channel)
    print "gas value"
    print(data)
    data = getReading(temp_channel)
    print "temp value"
    print(data)
    print "-------------------------------"

    sleep(1)
