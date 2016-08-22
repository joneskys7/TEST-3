import RPi.GPIO as GPIO 

import time

import spidev

import time

import os

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(40,GPIO.IN)

GPIO.setup(37,GPIO.OUT)

GPIO.output(37,False)

# Open SPI bus 

spi = spidev.SpiDev() 

spi.open(0,0)

# Function to read SPI data from MCP3008 chip

 # Channel must be an integer 0-7

def ReadChannel(channel):

	adc = spi.xfer2([1,(8+channel)<<4,0])

	data = ((adc[1]&3) << 8) + adc[2] 

	return data 
count=0

# Define sensor channels 

gas_channel = 0

# Define delay between readings 

delay = 5

for i in range(3):

# Read the gas sensor data 

	gas_level = ReadChannel(gas_channel)

# Print out results 

	print "--------------gas_value------------------------------"
	
        print("Gas: {}".format(gas_level))
		
	GPIO.output(37,True) 

for i in range (3): 
	
	if GPIO.input(40)==0: 
		
		print"Normal Rain" 
		
		GPIO.output(37,False) 
		
		time.sleep(1) 

		count=count+1
        if(count>=5):

		print "Heavyy Rain" 

		print "SOUND ON" 

		GPIO.output(37,True) 

		time.sleep(1)

		GPIO.output(37,False)


	else: 
		print"No Rain"

		print"SOUND OFF" 

		GPIO.output(37,False) 

		time.sleep(1)

		count=0
		
	

# Wait before repeating loop time.sleep(delay) GPIO.cleanup()

time.sleep(4)

GPIO.cleanup()
