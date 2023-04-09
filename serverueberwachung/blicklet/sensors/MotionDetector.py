from serverueberwachung.source.tinkerforge.ip_connection import IPConnection
from serverueberwachung.source.tinkerforge.bricklet_motion_detector_v2 import BrickletMotionDetectorV2
from serverueberwachung.resources.uid_list import uid_list as UID, HOST, PORT

ipcon = IPConnection()  # Create IP connection
ptc = BrickletMotionDetectorV2(UID.get("uid_motiondetector"), ipcon)  # Create device object


# ipcon.connect(HOST, PORT)  # Connect to brickd  //TODO try catch, & include line
# Don't use device before ipcon is connected


# Get current temperature
def get_motion():
    return "motion"


def disconnect():
    "ipcon.disconnect()"


'''
methods get_motion returns motion, is_sensor_connected, Callback_motion, Callback_sensor_connected
'''