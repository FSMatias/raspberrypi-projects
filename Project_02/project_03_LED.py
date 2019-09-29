# Control LED from Adafruit IO

import RPi.GPIO as GPIO
import time
from Adafruit_IO import Client, Feed, RequestError

# You can get your username and AIO Key from the Adafruit IO page
ADAFRUIT_IO_KEY = '<YOUR-AIO-KEY>' 
ADAFRUIT_IO_USERNAME = '<YOUR-USERNAME>'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
feed = aio.feeds('control-led-feed') # Get Feed

# LED is connected to OUT port 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# LED initial state is OFF
led_value = False
GPIO.output(18, led_value)

while True: 
    data = aio.receive(feed.key) 
    if data.value == 'ON': 
        led_value = True 
        print('received <- ON\n') 
    elif data.value == 'OFF': 
        led_value = False 
        print('received <- OFF\n') 
    else: 
        led_value = False
        print('Unexpected value: ' + data.value)

    # set the LED to the feed value 
    GPIO.output(18, led_value) 
    
    # timeout so we dont flood adafruit-io with requests 
    time.sleep(0.5)