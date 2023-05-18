from digitalio import DigitalInOut, Direction
import board
from pwmio import PWMOut
import time 

L1 = DigitalInOut(board.D2)
L2 = PWMOut(board.D3)
L1.direction = Direction.OUTPUT

R1 = DigitalInOut(board.D8)
R2 = PWMOut(board.D9)
R1.direction = Direction.OUTPUT

while True: 
    L1.value = True
    L2.duty_cycle=0

    R1.value = True
    R2.duty_cycle=0