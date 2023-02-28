import time
from wlkata_mirobot import WlkataMirobot
from time import sleep



def start_process(cmd_queue):
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
    arm = WlkataMirobot(portname="/dev/ttyUSB0")
    arm.unlock_all_axis()
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

def move(x, y, z, a, b, c):
    '''
    Move the robot by a the defined contrains above
    '''
    # arm controls
    arm = WlkataMirobot(portname="/dev/ttyUSB0")
    arm.unlock_all_axis()
    arm.go_to_axis(x, y, z, a, b, c)
    print("Successfully moved the robot")
    


if __name__ == "__main__":
    print("directly running the robot.py script")
    #leftRight()
    #arm.pump_off()
    home()
    
