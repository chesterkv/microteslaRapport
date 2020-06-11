import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

echo = 18
trig = 16

gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

stop = 1
v = 34000 #vitesse du son en cm.s-1
while stop != 0:
	#on met le trigger à HIGH pendant 10 microsecondes
	gpio.output(trig,True)
	time.sleep(0.00001)
	gpio.output(trig,False)
	#on récupère la distance en comptant le temps que met le signal à revenir
	start = time.time()
	while gpio.input(echo) == False:
		start = time.time()
	while gpio.input(echo) == True:
		end = time.time()

	dist = (end-start)*v/2
	print('Distance = '+str(dist))
	stop = input("continuer ?")
gpio.cleanup()
