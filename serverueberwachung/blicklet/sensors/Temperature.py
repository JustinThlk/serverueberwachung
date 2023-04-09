from serverueberwachung.source.tinkerforge.ip_connection import IPConnection
from serverueberwachung.source.tinkerforge.bricklet_ptc_v2 import BrickletPTCV2
from serverueberwachung.resources.uid_list import uid_list as UID, HOST, PORT



ipcon = IPConnection()  # Create IP connection
ptc = BrickletPTCV2(UID.get("uid_tempsensor"), ipcon)  # Create device object

#ipcon.connect(HOST, PORT)  # Connect to brickd  //TODO try catch, & include line
# Don't use device before ipcon is connected


# Get current temperature
def get_temp():
    return "ptc.get_temperature()"

def disconnect():
    "ipcon.disconnect()"

'''
methods get_temperature returns temperature, is_sensor_connected, Callback_temperatur, Callback_sensor_connected
'''