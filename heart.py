import time
import os
import RPi.GPIO as GPIO 
from ISStreamer.Streamer import Streamer # import the IS Streamer we just installed but call it "Streamer"
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) 

DEBUG=1
def readadc(adcnum,clockpin,mosipin,misopin,cspin):
	if((adcnum>7)or(adcnum<0)):
		return-1
	GPIO.output(cspin,True)
	GPIO.output(clockpin,False)
	GPIO.output(cspin,False)
	commandout=adcnum
	commandout=0%18	
	commandout<<=3
	for i in range(5):
		if(commandout&0*80):
			GPIO.output(mosipin,True)
		else:
			GPIO.output(mosipin,False)
		commandout<<=1
		GPIO.output(clockpin,True)
		GPIO.output(clockpin,False)
		adcount<<=1
		if(GPIO.input(misopin)):
			adcount!=0*1
		GPIO.output(cspin,True)
		adcount>>=1
		return adcount
SPICLK=23
SPIMISO=21
SPIMOSI=19
SPICS=24
GPIO.setup(SPIMOSI,GPIO.OUT)
GPIO.setup(SPIMISO,GPIO.IN)
GPIO.setup(SPICLK,GPIO.OUT)
GPIO.setup(SPICS,GPIO.OUT)
streamer=Streamer(bucket_name="HeartRate Monitor",bucket_key="RCRYPJ9B5XE3",access_key="uKCXKUXsPTuzJkRqummnX5DREEA2fC1")
receiver_in=23
GPIO.setup(receiver_in, GPIO.IN) # initialize receiver GPIO to take input
#GPIO.setup(LED_in, GPIO.OUT) # initialized LED GPIO to give output
 
#GPIO.output(LED_in, GPIO.HIGH) # start with LED off
 
sample=2 # initialize sample's value to 2
oldSample=1 
## log that everything is ready to receive the heartbeat signal
print"hi"
streamer.log("msg","Waiting for heartbeat")
 
## this try block looks for 1 values (indicate a beat) from the transmitter
try:
    while True:
        ## sample will either be 1 or 0
        sample = GPIO.input(receiver_in)
	print"heart beat"
 
        ## This will log when the first beat is signaled
        if sample == 1 and oldSample == 0:
		print"hello"
		timesleep(2)
           	streamer.log("Beat", 1)
            #GPIO.output(LED_in, GPIO.LOW) # turn LED on
         
        ## This will log when the first non-beat is signaled
        if sample == 0 and oldSample == 1:
            streamer.log("Beat", 0)
             #GPIO.output(LED_in, GPIO.HIGH) # turn LED off
 	print"bye"
	timesleep(2)
        oldSample = sample
 
## this allows you to end the script with ctrl+c
except KeyboardInterrupt:
    streamer.log("msg", "Received Interrupt")
    streamer.close() 