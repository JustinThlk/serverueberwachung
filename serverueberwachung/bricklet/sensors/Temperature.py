from serverueberwachung.source.tinkerforge.ip_connection import IPConnection
from serverueberwachung.source.tinkerforge.bricklet_ptc_v2 import BrickletPTCV2
from serverueberwachung.resources.uid_list import HOST, PORT, uid_list as UID


from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ptc_v2 import BrickletPTCV2

class temp_sensor:

    def __init__(self):
        self.ipcon = IPConnection() # Create IP connection
        self.ptc = BrickletPTCV2(UID["uid_tempsensor"], self.ipcon) # Create device object
        self.ipcon.connect(HOST, PORT) # Connect to bricklet
        self.max_temp = 0
        self.min_temp = 0
        self.options = ""
        self.period = 0
        self.value_has_to_change = False


    # def setup(self):
    #    self.ptc.set_temperature_callback_configuration(period=self.period,
    #                                                   max=self.max_temp,
    #                                                    min=self.min_temp,
    #                                                    option=self.options,
    #                                                    value_has_to_change=self.value_has_to_change)

    # Get current temperature
    def get_temp(self):
        ipcon = IPConnection()  # Create IP connection
        ptc = BrickletPTCV2(("Wcg", ipcon))  # Create device object

        ipcon.connect("172.20.10.54", 4233)  # Connect to brickd
        # Don't use device before ipcon is connected

        temperature = ptc.get_temperature()
        return str(temperature / 100.0) + " °C"

        # temperature = self.ptc.get_temperature()
        # return str(temperature/100.0) + " °C"

    def is_connected(self):
        return self.ptc.is_sensor_connected()

    def get_temp_at_period(self, period):
        self.period = period
        "self.setup()"

    def disconnect(self):
        self.ipcon.disconnect()


'''
methods get_temperature returns temperature, is_sensor_connected, Callback_temperatur, Callback_sensor_connected
'''