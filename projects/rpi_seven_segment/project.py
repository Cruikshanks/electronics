import RPi.GPIO as GPIO

# Needed to allow the program to `sleep` for 1 second after displaying a digit.
# Else the display will be more like a light show!
import time

GPIO.setmode(GPIO.BCM)

# Dictionary of GPIO pins used and the segment they correspond to
pins = {'a': 17, 'b': 22, 'c': 6, 'd': 13, 'e': 19, 'f': 27, 'g': 5}

# Dictionary of digits to display on the 7 segment display. For each
# digit we hold an array of which segments need to be lit.
digits = {
    0: ['a', 'b', 'c', 'd', 'e', 'f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'g', 'e', 'd'],
    3: ['a', 'b', 'c', 'd', 'g'],
    4: ['b', 'c', 'f', 'g'],
    5: ['a', 'c', 'd', 'f', 'g'],
    6: ['a', 'c', 'd', 'e', 'f', 'g'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'f', 'g']
}


def renderDigit(digit):
    # Turn off all the segments
    GPIO.output(list(pins.values()), GPIO.LOW)

    # Get the array of segments that need switching on for this digit
    digitSegments = digits[digit]

    # Iterate through the array of segments, locate the corresponding GPIO pin
    # and by setting it to GPIO.HIGH, turn on the segment
    for segment in digitSegments:
        GPIO.output(pins[segment], GPIO.HIGH)


try:
    # Tell RPi we won't be reading from the pins. Instead will be sending data
    # out (by way of whether the voltage is high or low)
    GPIO.setup(list(pins.values()), GPIO.OUT)

    # Turn off all the segments
    GPIO.output(list(pins.values()), GPIO.LOW)

    # Start by displaying 0
    digit = 0

    # Just keep looping until the CTRL+C is entered
    while True:
        renderDigit(digit)
        print("Displaying " + str(digit))

        # If digit is 9 reset to 0, else just add 1 to it
        digit = 0 if digit == 9 else (digit + 1)

        # Sleep for 1 second, to give us a chance to see the digit displayed
        time.sleep(1)
except KeyboardInterrupt:
    print("Goodbye")
finally:
    GPIO.cleanup()
