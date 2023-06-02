from digitalio import DigitalInOut, Direction
import board
from pwmio import PWMOut
import adafruit_hcsr04
import time 

#assigning pins to motors
L1 = PWMOut(board.D2)
L2 = PWMOut(board.D3)

R1 = PWMOut(board.D8)
R2 = PWMOut(board.D9)

#assigning pins to sensors
Lsens = adafruit_hcsr04.HCSR04(trigger_pin=board.A4, echo_pin=board.A5)
Rsens = adafruit_hcsr04.HCSR04(trigger_pin=board.A0, echo_pin=board.A1)



while True: 
    try:
        #creating variables to use sensor values
        lcm=Lsens.distance
        rcm=Rsens.distance

        if rcm > 15 and lcm < 15: #if object is closer to left sensor
            L1.duty_cycle=65000 
            L2.duty_cycle=0 #left motor backwards

            R1.duty_cycle=0 #right motor forwards
            R2.duty_cycle=65000 
            print("turn left")

        if lcm > 15 and rcm < 15: #if object is closer to right sensor
            L1.duty_cycle=0 #left motor forwards
            L2.duty_cycle=65000 

            R1.duty_cycle=65000
            R2.duty_cycle=0 #right motor backwards
            print("turn right")

        if lcm > 15 and rcm > 15: #if object is farther than 15cm away
            L1.duty_cycle=0 #left motor forwards
            L2.duty_cycle=65000
            
            R1.duty_cycle=0 #right motor forwards
            R2.duty_cycle=65000
            print("forward")

        if lcm < 15 and rcm < 15: #if object is closer than 15cm
            L1.duty_cycle=65000
            L2.duty_cycle=0 #left motor backwards

            R1.duty_cycle=65000
            R2.duty_cycle=0 #right motor backwards
            print("backward")
    except RuntimeError:
        print("retrying!")
        time.sleep(0.1)
