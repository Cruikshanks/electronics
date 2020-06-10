import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

try:
    while True:
        if GPIO.input(16) == 0:
            print("Open")
        else:
            print("Closed")
finally:
    GPIO.cleanup()
