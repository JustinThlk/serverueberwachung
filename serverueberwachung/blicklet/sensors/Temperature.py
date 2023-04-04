from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ptc_v2 import BrickletPTCV2
from serverueberwachung.resources.uid_list import uid_tempsensor as UID, HOST, PORT

ipcon = IPConnection()  # Create IP connection
ptc = BrickletPTCV2(UID, ipcon)  # Create device object

ipcon.connect(HOST, PORT)  # Connect to brickd
# Don't use device before ipcon is connected


# Get current temperature
def getTemp():
    return ptc.get_temperature()
