from serverueberwachung.source.tinkerforge.ip_connection import IPConnection
from serverueberwachung.source.tinkerforge.bricklet_ptc_v2 import BrickletPTCV2
from serverueberwachung.resources.uid_list import HOST, PORT, uid_list as UID

class temp_sensor:

    #ipcon = IPConnection()  # Create IP connection
    #ptc = BrickletPTCV2(UID.get("uid_tempsensor"), ipcon)  # Create device object
    #ipcon.connect(HOST, PORT)
    max_temp = 0
    min_temp = 0
    options = ""
    period = 0
    value_has_to_change = False


    #def setup(self):
    #    self.ptc.set_temperature_callback_configuration(period=self.period,
    #                                                   max=self.max_temp,
    #                                                    min=self.min_temp,
    #                                                    option=self.options,
    #                                                    value_has_to_change=self.value_has_to_change)

    # Get current temperature
    def get_temp(self):
        return "self.ptc.get_temperature()"

    def is_connected(self):
        return "self.ptc.is_sensor_connected()"

    def get_temp_at_period(self, period):
        self.period = period
        "self.setup()"

    #def disconnect(self):
    #    self.ipcon.disconnect()


'''
methods get_temperature returns temperature, is_sensor_connected, Callback_temperatur, Callback_sensor_connected
'''