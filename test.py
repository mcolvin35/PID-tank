from digitalio import DigitalInOut, Direction
import board
from pwmio import PWMOut
import time 

L1 = PWMOut(board.D2)
L2 = PWMOut(board.D3)

while True: 
    L1.duty_cycle=0
    L2.duty_cycle=0