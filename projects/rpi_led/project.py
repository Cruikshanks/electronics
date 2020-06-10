import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

led_state = False

try:
    while True:
        GPIO.output(18, led_state)

        if led_state:
            print("The LED is on. Press 'enter' to switch it off")
        else:
            print("The LED is off. Press 'enter' to switch it on")

        arg = input("Press 'q' then 'enter' to quit.")
        if arg == "q":
            exit()
        elif led_state:
            led_state = False
        else:
            led_state = True
finally:
    GPIO.cleanup()
