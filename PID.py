from PID_CPY import PID 
import board
from pwmio import PWMOut
import adafruit_hcsr04
import time 

pid = PID(1000, 100, 50, setpoint=15, output_limits=(0, 65535))
dis=0


L1 = PWMOut(board.D2)
L2 = PWMOut(board.D3)

R1 = PWMOut(board.D8)
R2 = PWMOut(board.D9)

Lsens = adafruit_hcsr04.HCSR04(trigger_pin=board.A4, echo_pin=board.A5)
Rsens = adafruit_hcsr04.HCSR04(trigger_pin=board.A0, echo_pin=board.A1)



while True: 
    try:
        dis = ((Lsens.distance+Rsens.distance)/2.0)
        control = pid(dis)
        motor=int(control)
        p,i,d = pid.components

        print("DISTANCE:", dis,"\t", p,i,d, "\t MOTOR:", control) 
        #print("\t", pid.proportional, pid.integral, pid.derivative)
        
        # lcm=Lsens.distance
        # rcm=Rsens.distance

       # if rcm > 15 and lcm < 15:
        L1.duty_cycle=motor
        L2.duty_cycle=65000

        R1.duty_cycle=motor
        R2.duty_cycle=65000

        # if lcm > 15 and rcm < 15:
        #     L1.duty_cycle=control
        #     L2.duty_cycle=65000

        #     R1.duty_cycle=65000
        #     R2.duty_cycle=control
        #     print("turn right")

        # if lcm > 15 and rcm > 15: 
        #     L1.duty_cycle=0
        #     L2.duty_cycle=65000

        #     R1.duty_cycle=0
        #     R2.duty_cycle=65000
        #     print("forward")

        # if lcm < 15 and rcm < 15: 
        #     L1.duty_cycle=65000
        #     L2.duty_cycle=0

        #     R1.duty_cycle=65000
        #     R2.duty_cycle=0
        #     print("backward")
    except RuntimeError:
        print("retrying!")
        time.sleep(0.1)
