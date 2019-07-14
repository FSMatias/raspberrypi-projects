import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, False) #LED inital state is OFF

while True:
    button_state = GPIO.input(17)
    if button_state == False:
        # When button is pressed, LED is turned ON
        print('Button Pressed')
        GPIO.output(18, True)
        time.sleep(0.2)
    else:
        GPIO.output(18, False)