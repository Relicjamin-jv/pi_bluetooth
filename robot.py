import time
from wlkata_mirobot import WlkataMirobot
from time import sleep


arm = WlkataMirobot(portname="/dev/ttyUSB0")
arm.unlock_all_axis()


def home():
    print("Instantiate the Mirobot Arm instance")
    arm = WlkataMirobot()
    # Mirobot Arm Multi-axis executing
    print("Homing start")
    # Note:
    # - In general, if there is no seventh axis, just execute arm.home(),
    # has_slider parameter is set to False by default
    # - If there is a slider (axis 7), set has_slider to True
    arm.home()
    # arm.home(has_slider=False)
    # arm.home(has_slider=True)
    print("Homing finish")
    # Status Update and Query
    print("update robotic arm status")
    arm.get_status()
    print(f"instance status after update: {arm.status}")
    print(f"instance status name after update: {arm.status.state}")
    pass

def leftRight():
    #arm.go_to_axis(30,0,0,0,0,0,1500)   #The first axis rotates from the zero position to the absolute position + 30 at 1500°/min
    arm.go_to_axis(-20,0,0,0,0,0)   #The first axis rotates from the zero position to the absolute position -30 at 1500°/min
    #arm.go_to_zero()   

def blowAir():

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
    print("directly running the robot.py script")
    #leftRight()
    #arm.pump_off()
    home()
    
