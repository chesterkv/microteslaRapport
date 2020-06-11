import time
import RPi.GPIO as GPIO
cest tout faux (pour les hertz notamment)
freq = input("frequence = ")
cycle = input("cycle en pourcent = ")
gpio_out = input("gpio de sortie = ")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(gpio_out,GPIO.OUT)

def signal(freq,cycle):
	stop = cycle*freq/100
	start = time.time()
	while time.time() < (start+1):
		GPIO.output(gpio_out,GPIO.HIGH)
		time.sleep(stop)
		GPIO.output(gpio_out,GPIO.LOW)
		time.sleep(freq-stop)
