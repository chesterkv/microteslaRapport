import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin = 22

GPIO.setup(pin,GPIO.OUT)
while True:
	a = input("1/0")
	if a == 1:
		GPIO.output(pin,True)
	else:
		GPIO.output(pin,False)

