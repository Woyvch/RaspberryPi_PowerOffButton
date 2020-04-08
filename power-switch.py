#!/usr/bin/env python
"""Script for shutdown and reboot"""

from gpiozero import Button, LED
from signal import pause
from subprocess import call

__author__ = "Wouter Scherpereel"

# the if-statement will be executed when this is the main-program
if __name__ == '__main__':
    def Shutdown():
        """Shutdown the raspberry Pi"""
        call('sudo shutdown -h now', shell=True)

    def WhenPressed():
        """starts blinking with 1/2 second rate"""
        led.blink(on_time=0.5, off_time=0.5)

    def WhenReleased():
        """turn the led off when the button is released"""
        led.off()

    led = LED(4)
    # the length (in seconds) to wait after the device is activated
    holdTime = 3
    button = Button(3, hold_time=holdTime)
    # The function to run when the button is presses/released
    button.when_pressed = WhenPressed
    button.when_released = WhenReleased
    # The function to run when the device remained active for hold_time seconds
    button.when_held = Shutdown
    # keeps the script running until it is terminated (never)
    pause()