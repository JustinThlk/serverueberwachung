from serverueberwachung.source.tinkerforge.ip_connection import IPConnection
from serverueberwachung.source.tinkerforge.bricklet_humidity_v2 import HumidityV2
from serverueberwachung.resources.uid_list import uid_list as UID, HOST, PORT

ipcon = IPConnection()  # Create IP connection
ptc = HumidityV2(UID.get("uid_humidity"), ipcon)  # Create device object


# ipcon.connect(HOST, PORT)  # Connect to brickd  //TODO try catch, & include line
# Don't use device before ipcon is connected


# Get current temperature
def get_humidity():
    return "humidity"


def disconnect():
    "ipcon.disconnect()"


'''
methods get_motion returns humidity, is_sensor_connected, Callback_humidity, Callback_sensor_connected
'''