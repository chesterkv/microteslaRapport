import RPi.GPIO as GPIO
import time
pwm_gpio = 12
frequence = 50
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pwm_gpio,GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio,frequence)
stop = 1
pwm.start(0)
while True:
	stop = input("continuer ?")
	if stop == 0:
		break
	angle = input("angle")
	pwm.ChangeDutyCycle(angle)
pwm.stop()
GPIO.cleanup
