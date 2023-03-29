import time
from wlkata_mirobot import WlkataMirobot
from time import sleep

arm = None

def start_process(cmd_queue):
    home()
    while True:
        if cmd_queue.empty() == False:
            print("Getting next command")
            command = cmd_queue.get()
            print(f"Working on command: {command}")
            move(command[0], command[1], command[2], command[3], command[4], command[5])
            print(f"Finished command: {command}")
            cmd_queue.task_done() # releases the lock on the queue


def home():
    # arm controls
    #arm = WlkataMirobot(portname="/dev/ttyUSB0")
    arm.unlock_all_axis()
    print("Instantiate the Mirobot Arm instance")
    # arm = WlkataMirobot()
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

def my_go_to_axis(x=None, y=None, z=None):
	# instruction = 'M21 G90'  # X{x} Y{y} Z{z} A{a} B{b} C{c} F{speed}
    # instruction = 'M20 G90 G00'  # X{x} Y{y} Z{z} A{a} B{b} C{c} F{speed}
    instruction = 'M20 G90 G00 F2000'
    pairings = {'X': x, 'Y': y, 'Z': z}
    msg = arm.generate_args_string(instruction, pairings)
    return arm.send_msg(msg, wait_ok=True, wait_idle=True)


def move(x, y, z, a = 0, b = 0, c = 0):
    '''
    Move the robot by a the defined contrains above
    '''
    # arm controls
   
    arm.unlock_all_axis()
    arm.go_to_axis(x, y, z, a, b, c)
    print("Successfully moved the robot")
    


if __name__ == "__main__":
    print("directly running the robot.py script")
    #leftRight()
    #arm.pump_off()
    arm = WlkataMirobot(portname="/dev/ttyUSB0")
    home()
    print('after home, start to go to axis')
    my_go_to_axis(y=210, x=0, z=50)
    print('before home, finish go to axis')
   # my_go_to_axis(x=210, y=0, z=100)
    arm.gripper_open() 
    #my_go_to_axis(x=150, y=150, z=75)
    arm.gripper_close()
    #home()
    
