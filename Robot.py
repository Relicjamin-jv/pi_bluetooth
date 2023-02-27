import time
from wlkata_mirobot import WlkataMirobot
from time import sleep
import time

arm = WlktaMicrobot(portname = "/dev/ttyUSB0")

def home():
    print("Instantiate the Mircobot Instance")
    arm = WlktaMicrobot()

    print("Homing Start")
    arm.home()

    print("Homing Finish")
    print("Update Robot Arm Status")
    arm.get_status()
    print(f"Instance status after update: {arm.status}")
    print(f"Instance status name after update: {arm.status.state}")
    pass

def leftRight():
    arm= WlktaMicrobot()
    arm.home_simultaneous()          #Home Mirobot
    sleep(15)                       #Delay 15s
    for i in range(10):                #Repeat the following actions 10 times
        arm.go_to_axis(30,0,0,0,0,0,1500)   #The first axis rotates from the zero position to the absolute position + 30 at 1500°/min
        arm.go_to_axis(-30,0,0,0,0,0,1500)   #The first axis rotates from the zero position to the absolute position -30 at 1500°/min
        arm.go_to_zero()   

def blowAir():
    arm = WlkataMirobot()
    arm.home()

    # Air Pump Start - Suction
    arm.pump_suction()
    # Delay 5s
    time.sleep(5)

    # Air Pump Off
    arm.pump_off()
    # Delay 5s
    time.sleep(2)

    # Air Pump Start - Blowing
    arm.pump_blowing()
    # Delay 5s
    time.sleep(5)

    # Air Pump Off
    arm.pump_off()
    # Delay 5s
    time.sleep(2)
pass

if __name__ == "__main__":
    print("Directly running the robot.py script")
    home()
