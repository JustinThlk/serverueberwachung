from serverueberwachung.source.tinkerforge.ip_connection import IPConnection
from serverueberwachung.source.tinkerforge.bricklet_ambient_light_v3 import AmbientLightV3
from serverueberwachung.resources.uid_list import uid_list as UID, HOST, PORT

ipcon = IPConnection()  # Create IP connection
ptc = AmbientLightV3(UID.get("uid_ambientlight"), ipcon)  # Create device object


# ipcon.connect(HOST, PORT)  # Connect to brickd  //TODO try catch, & include line
# Don't use device before ipcon is connected


# Get current temperature
def get_ligth():
    return "light"


def disconnect():
    "ipcon.disconnect()"


'''
methods get_motion returns light, is_sensor_connected, Callback_light, Callback_sensor_connected
'''