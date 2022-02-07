# Author: Megana Boddam
# CSS 532: IoT Final Project: lightSense
# Date: 12/9/2021
# Goal: Program to be executed on Raspberry Pi 
#       to test solenoid movement. 

import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

# pin for solenoid in/out was on GPIO17
gpio.setup(17, gpio.OUT)

while(True):
    gpio.output(17, 1)
    print("Solenoid coiled up")
    sleep(2)
    gpio.output(17, 0)
    print("Solenoid punched out")
    sleep(2)