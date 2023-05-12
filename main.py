from digitalio import DigitalInOut, Direction
import board
from pwmio import PWMOut

L1 = PWMOut(board.D2)
L2 = DigitalInOut(board.D3)
L2.direction = Direction.OUTPUT

R1 = PWMOut(board.D8)
R2 = DigitalInOut(board.D9)
R2.direction = Direction.OUTPUT

while True: 
    L1.duty_cycle=0
    L2.value=True
    R1.duty_cycle=0
    R2.value=True
    print("left forward")