# Author: Megana Boddam
# CSS 532: IoT Final Project: lightSense
# Date: 12/9/2021
# Goal: Program to be executed on Raspberry Pi to test motion sensor. 

from gpiozero import MotionSensor

# pin for motion sensor voltage outputs was on GPIO4
pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("you moved")
    pir.wait_for_no_motion()
    print("you stopped moving")
