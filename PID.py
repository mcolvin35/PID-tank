from PID_CPY import PID 
import board
from pwmio import PWMOut
import adafruit_hcsr04

pid = PID(10, 0, 1, setpoint=15, output_limits=(-65535, 65535))
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
        p,i,d = pid.components

        print("DISTANCE:", dis,"\t", p,i,d, "\t MOTOR:", control) 
        
        lcm=Lsens.distance
        rcm=Rsens.distance

        if control < 0:
            L1.duty_cycle=abs(int(control))
            L2.duty_cycle=65535

            R1.duty_cycle=abs(int(control))
            R2.duty_cycle=65535

        if control > 0:
            L1.duty_cycle=65535
            L2.duty_cycle=abs(int(control))

            R1.duty_cycle=65535
            R2.duty_cycle=abs(int(control))
    except RuntimeError:
        print("Retrying!")
