#Single Button Starter code
# This code controls a button that with two terminals (one attached to GND and one attached to the GP10 pin) to print in the serial monitor when pressed.

import board
import digitalio
import time

score_button = digitalio.DigitalInOut(board.GP10)
score_button.direction = digitalio.Direction.INPUT
score_button.pull = digitalio.Pull.UP

score_button.value

print(score_button.value)

while True:
    print(score_button.value)
    if score_button.value == False:
        print("Button is pressed")
        time.sleep(0.5)
    else:
        print("Button not pressed")
        time.sleep(0.5)



