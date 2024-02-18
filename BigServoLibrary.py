from machine import Pin, PWM
from time import sleep

class BigServo:
    def __init__(self, pinNum=12, frequency=50):
        self.minDuty = 2000
        self.maxDuty = 8500
        self.bigBoy = PWM(Pin(pinNum))
        self.bigBoy.freq(frequency)
    
    def minOut(self):
        self.bigBoy.duty_u16(self.minDuty)
        sleep(1)
    
    def maxOut(self):
        self.bigBoy.duty_u16(self.maxduty)
        sleep(1)
    
    def fullSweep(self):
        self.bigBoy.duty_u16(self.minDuty)
        sleep(1)
        self.bigBoy.duty_u16(self.maxDuty)
        sleep(1)
        self.bigBoy.duty_u16(self.minDuty)
