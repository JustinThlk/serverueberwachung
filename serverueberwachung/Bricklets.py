from tinkerforge.ip_connection import IPConnection

import resources as resc
from tinkerforge.bricklet_ptc_v2 import BrickletPTCV2
from tinkerforge.bricklet_motion_detector_v2 import BrickletMotionDetectorV2
from tinkerforge.bricklet_ambient_light_v3 import BrickletAmbientLightV3
from tinkerforge.bricklet_humidity_v2 import BrickletHumidityV2

class Bricklets:
    def __init__(self):
        ipcon = IPConnection()
        self.TemperatureSensor = BrickletPTCV2(resc.uid_list["tempsensor"], ipcon)
        self.MotionDetector = BrickletMotionDetectorV2(resc.uid_list["motiondetector"], ipcon)
        self.LightSensor = BrickletAmbientLightV3(resc.uid_list["ambientlight"], ipcon)
        # self.HumiditySensor = BrickletHumidityV2(resc.uid_list["humidity"], resc.ipcon_Humidity)
        ipcon.connect(resc.HOST, resc.PORT)
        # Don't use device before ipcon is connected
