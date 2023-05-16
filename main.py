from digitalio import DigitalInOut, Direction
import board
from pwmio import PWMOut
import adafruit_hcsr04
import time 


Lsens = adafruit_hcsr04.HCSR04(trigger_pin=board.A4, echo_pin=board.A5)
Rsens = adafruit_hcsr04.HCSR04(trigger_pin=board.A0, echo_pin=board.A1)



while True: 
    try:
        lcm=Lsens.distance
        rcm=Rsens.distance

        if lcm < 15:
            L1 = PWMOut(board.D2)
            L2 = PWMOut(board.D3)
            L1.duty_cycle=65000
            L2.duty_cycle=0

            R1 = PWMOut(board.D8)
            R2 = PWMOut(board.D9)
            R1.duty_cycle=0
            R2.duty_cycle=65000
            print("turn left")

        if rcm < 15:
            L1 = PWMOut(board.D2)
            L2 = PWMOut(board.D3)
            L1.duty_cycle=0
            L2.duty_cycle=65000
            R1 = PWMOut(board.D8)
            R2 = PWMOut(board.D9)
            R1.duty_cycle=65000
            R2.duty_cycle=0
            print("turn right")

        if lcm > 15 and rcm > 15: 
            L1 = PWMOut(board.D2)
            L2 = PWMOut(board.D3)
            L1.duty_cycle=0
            L2.duty_cycle=65000

            R1 = PWMOut(board.D8)
            R2 = PWMOut(board.D9)
            R1.duty_cycle=0
            R2.duty_cycle=65000
            print("forward")

        if lcm < 15 and rcm < 15: 
            L1 = PWMOut(board.D2)
            L2 = PWMOut(board.D3)
            L1.duty_cycle=65000
            L2.duty_cycle=0

            R1 = PWMOut(board.D8)
            R2 = PWMOut(board.D9)
            R1.duty_cycle=65000
            R2.duty_cycle=0
            print("backward")
    except RuntimeError:
        print("retrying!")
        time.sleep(0.1)
