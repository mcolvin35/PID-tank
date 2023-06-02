# ***PID TANKBOT***
## **Table of Contents**
* [Planning](#planning)
* [Design](#design)
* [Assembly](#assembly)
* [Code](#code)
* [Final Product](#final-product)

## **Planning**
### **Brainstorming**
My original idea for this project was to make a tank that followed an object forwards and backwards with PID. Eventually, that idea evolved into also having it turn to follow an object using two ultrasonic sensors angled away from each other. 


<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/sketch.JPG?raw=true" width="500"> 


Here's the original sketch for my design!


<img src="https://github.com/mcolvin35/PID-project/blob/master/images/PID%20idea.png?raw=true" width="300">

And here's a "more refined" version I made later

### **Materials**
* 1 Battery pack + 6 AA batteries
* 1 Adafruit M4 Metroexpress board
* 1 Arduino prototyping shield
* 1 Arduino mini breadboard
* 2 Adafruit HCSR04 ultrasonic sensors
* 1 Adafruit DRV8833 H-bridge
* 2 Adafruit DC gearbox motors
* 2 Lego rubber tank tranks
* 6 3D printed wheels 
* 1 3D printed frame
* 4 10mm diameter bearings
* 7 male-male jumper wires
* 8 male-female jumper wires
* 1 switch
* 2 #4-40x0.375" socket head screws
* 2 #4-40x0.375" button head screws
* 4 #4-40x1" socket head screws
* 4 #1-72x0.375" socket head screws
* 4 #1-72 hex nuts

## **Design**
[Here's a link to the Onshape document](https://cvilleschools.onshape.com/documents/8fae5fdf447fbfb9d54d9470/w/7d247cc5ccc396c5e0c210bc/e/ef00bd4d61704b1228024abc?renderMode=0&uiState=6479561290e9b5185ed82d96)

<p align="center">
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/isometric.png?raw=true" width="8000">

<p align="left">
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/front.png?raw=true" width="375"><img src="https://github.com/mcolvin35/PID-tank/blob/master/images/side.png?raw=true" width="375">

<p align="left">
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/back.png?raw=true" width="375"><img src="https://github.com/mcolvin35/PID-tank/blob/master/images/top.png?raw=true" width="375">

## **Assembly**

### **First motor test**
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/tread_test.gif?raw=true" width="400"> 

This was just a simple test to see if my treads were working after I got the wheels on. It kind of worked but the treads were a little loose and the teeth on the treads were skipping so I made the wheels and the empty space between the wheel teeth bigger. 

### **First drive test**
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/drive_test.gif?raw=true" width="400"> 

This was the first time it drove on its own. I had just wired up the battery pack and gotten the board in place. The reason it goes slightly to the left is because the left wheels are the newer version while the right wheels are still the old version. That's also why the tread comes off at the end.

### **Sensor test**
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/noPID_v1.gif?raw=true" width="400"> 

At this point, the assembly is pretty much complete. This was after wiring up the sensors and writing some simple code to make it follow my hand. It doesn't go backwards very smoothly because of some errors in the code that I had to fix.

### **Wiring Diagram**
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/wiringdiagramv2.png?raw=true" width="1000"> 

## **Code**
I ended up having two different versions of the code. One version had no PID but could turn and follow objects, the other had PID but could only got forwards and backwards. I wish I could've done more with the PID version but sadly I ran out of time. 

### **Non-PID**
```python 
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

```
### **PID**
```python
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
```
## **Final Product**
So here is the "final" product! 
### **Non-PID**
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/noPID_final.gif?raw=true" width="400"> 

You can see how this version moves backwards much faster than the other one. 

### **PID**
<img src="https://github.com/mcolvin35/PID-tank/blob/master/images/PID_final.gif?raw=true" width="400"> 

And here's the sort of unfinished PID version. This one doesn't move forwards very well. You can't see it in the GIF but it does still to tend to oscillate a bit when it's trying to stand still. 

### **Reflection**
Overall, I'm really happy with how this project turned out! I do wish I could've had more time to work on tuning and troubleshooting the PID version, and also to clean up the aesthetics a bit, like color coding jumper wires, using shorter wires where I can, and tucking away some of the wires from the motors. I think I spent too much time focusing on the non-PID version and because of that I only had a few days to get the PID version set up. That being said, the non-PID version does work way better than I ever expected it to and I'm really happy about that! I'd say other than the time constraint, this whole project went pretty smoothly without any major hitches that held me back for a long time.

## **Thanks!**