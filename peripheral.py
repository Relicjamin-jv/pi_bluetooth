# Standard modules
from enum import IntEnum
import logging
import struct

# Bluezero modules
from bluezero import async_tools
from bluezero import adapter
from bluezero import peripheral

#from wrapper
import threading
from robot import start_process

import queue

PI_SRV = '0000181c-0000-1000-8000-00805f9b34fb' # name of the service
CMD_UUID = '00002a37-0000-1000-8000-00805f9b34fb' # name of the characteristic of that service, defined by bluetooth spec

# thread safe queue
cmd_queue = queue.Queue()

# takes in a byte array
def read_cmd(value, options):
    print("A command was sent")
    command = unwrap(value)
    print(f"Adding the robot command: {command}")
    cmd_queue.put_nowait(command)
    
    

def unwrap(input):
    return [-10, 10, -10, 5, 4, 3]

def main(adapter_addr):
    """
    Advertising and start the peripheral, and starts the robot loop
    """

    # starting the robot job queue
    print("staring the robot thread")
    robot_thread = threading.Thread(target=start_process, name="robot", args=(cmd_queue,))
    robot_thread.start()


    logger = logging.getLogger('localGATT')
    logger.setLevel(logging.DEBUG)

    # create the peripheral
    p_mon = peripheral.Peripheral(adapter_addr, local_name="PI Controller", appearance=0x002)

    # adding the reading service
    p_mon.add_service(srv_id=1, uuid=PI_SRV, primary=True)

    # add characteristics
    p_mon.add_characteristic(srv_id=1, chr_id=1, uuid=CMD_UUID, value=[], flags=['write'], write_callback=read_cmd, notify_callback=None, notifying=False) # this is from central perspective, we must write to the characteristic central

    p_mon.publish()

    

if __name__ == '__main__':
    print(list(adapter.Adapter.available())[0].address)
    main(list(adapter.Adapter.available())[0].address)


