# Author: Megana Boddam
# CSS 532: IoT Final Project: lightSense
# Date: 12/9/2021
# Goal: Program to be executed on Raspberry Pi to test light sensor. 

from gpiozero import LightSensor
from time import sleep

# pin for detecting light sensor output was on GPIO22
ldr = LightSensor(22, queue_len=3, charge_time_limit=0.02, threshold=0.8)

count = 0;
while True:
    print("waiting for light")
    ldr.wait_for_light()
    count += 1
    print("Light detected", count)
    sleep(2)