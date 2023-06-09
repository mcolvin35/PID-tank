from PID_CPY import PID 
import board
from pwmio import PWMOut
import adafruit_hcsr04

pid = PID(10, 0, 1, setpoint=15, output_limits=(-65535, 65535)) #pid tuning
dis=0

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
        dis = ((Lsens.distance+Rsens.distance)/2.0) #average distance between sensors
        control = pid(dis) #pid calculation 
        p,i,d = pid.components

        print("DISTANCE:", dis,"\t", p,i,d, "\t MOTOR:", control) #distance, pid, and pid output
        
        lcm=Lsens.distance
        rcm=Rsens.distance

        if control < 0: #if pid output is less than 0
            L1.duty_cycle=abs(int(control)) #left motor forwards absolute value of control (absolute value and int bc duty_cycle doesnt take negative numbers or decimals) 
            L2.duty_cycle=65535

            R1.duty_cycle=abs(int(control)) #right motor forwards
            R2.duty_cycle=65535

        if control > 0: #if pid output is greater than 0
            L1.duty_cycle=65535
            L2.duty_cycle=int(control)

            R1.duty_cycle=65535
            R2.duty_cycle=int(control)
    except RuntimeError:
        print("Retrying!")
