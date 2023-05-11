import digitalio
from analogio import AnalogIn, AnalogOut
import board

L1=AnalogOut(board.D7)
L2=AnalogOut(board.D6)

R1=AnalogOut(board.D10)
R2=AnalogOut(board.D11)

while True: 
    L1 = 30
    L2 = 1