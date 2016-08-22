import RPi.GPIO as GPIO
import time
import spidev
from time import sleep
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.IN)
spi = spidev.SpiDev()
spi.open(0,0)
sleepTime = 0.000
def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data
count=0
gas_channel = 0
for i in range(45678900):
    gas_level = ReadChannel(gas_channel)
    print "--------------------------------------------"
    print("Gas: {}".format(gas_level))
    sleep(sleepTime)

if (.format(gas_level)) = 5:
    print" hi"
    time.sleep(1)
else:
    print"bye"
GPIO.cleanup()
