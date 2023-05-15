from digitalio import DigitalInOut, Direction
import board
from pwmio import PWMOut
import adafruit_hcsr04
import time 


LS = adafruit_hcsr04.HCSR04(trigger_pin=board.A4, echo_pin=board.A5)
RS = adafruit_hcsr04.HCSR04(trigger_pin=board.A0, echo_pin=board.A1)



while True: 
    try:
        LCM=LS.distance
        RCM=RS.distance
    except RuntimeError:
        print("retrying!")
    time.sleep(0.1)


    if LCM < 15:
        L1 = DigitalInOut(board.D2)
        L2 = PWMOut(board.D3)
        L1.direction = Direction.OUTPUT
        L1.value=True
        L2.duty_cycle=0

        R1 = PWMOut(board.D8)
        R2 = DigitalInOut(board.D9)
        R2.direction = Direction.OUTPUT
        R1.duty_cycle=0
        R2.value=True
        print("turn left")

    if RCM < 15:
        L1 = PWMOut(board.D2)
        L2 = DigitalInOut(board.D3)
        L2.direction = Direction.OUTPUT
        L1.duty_cycle=0
        L2.value=True

        R1 = DigitalInOut(board.D8)
        R2 = PWMOut(board.D9)
        R1.direction = Direction.OUTPUT
        R1.value=True
        R2.duty_cycle=0
        print("turn right")

    if LCM > 15 and RCM > 15: 
        L1 = PWMOut(board.D2)
        L2 = DigitalInOut(board.D3)
        L2.direction = Direction.OUTPUT
        L1.duty_cycle=0
        L2.value=True

        R1 = PWMOut(board.D8)
        R2 = DigitalInOut(board.D9)
        R2.direction = Direction.OUTPUT
        R1.duty_cycle=0
        R2.value=True
        print("forward")

    if LCM < 15 and RCM < 15: 
        L1 = DigitalInOut(board.D2)
        L2 = PWMOut(board.D3)
        L1.direction = Direction.OUTPUT
        L1.value=True
        L2.duty_cycle=0

        R1 = DigitalInOut(board.D8)
        R2 = PWMOut(board.D9)
        R1.direction = Direction.OUTPUT
        R1.value=True
        R2.duty_cycle=0
        print("backward")
    