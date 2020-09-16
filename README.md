# RaspberryPi_PowerOffButton
An example how to use a power-off button for the Raspberry Pi

This is a short script to safely shutdown the Raspberry PI,
that way it is safe to cut the power without corrupting the SD-card.
I use a Raspberry Pi model 4.

Starting the script when the RPI boots with rc.local:
https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

Some inspiration I used:
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi
https://github.com/TonyLHansen/raspberry-pi-safe-off-switch/

An explication of the gpiozero library:
https://gpiozero.readthedocs.io

Coding guidelines for Python:
https://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting

I'm new to Python, so if something is not done right let me now pls 
