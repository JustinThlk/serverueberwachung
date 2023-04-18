from resources import HOST, PORT, uid_list as UID
from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_ptc_v2 import BrickletPTCV2
from tinkerforge.bricklet_motion_detector_v2 import BrickletMotionDetectorV2
from tinkerforge.bricklet_ambient_light_v3 import BrickletAmbientLightV3
from tinkerforge.bricklet_humidity_v2 import BrickletHumidityV2

class Bricklets:
    def __init__(self, ipcon):
        #ipcon = IPConnection()
        self.TemperatureSensor = BrickletPTCV2(UID["tempsensor"], ipcon)
        self.MotionDetector = BrickletMotionDetectorV2(UID["motiondetector"], ipcon)
        self.LightSensor = BrickletAmbientLightV3(UID["ambientlight"], ipcon)
        self.HumiditySensor = BrickletHumidityV2(UID["humidity"], ipcon)
        #ipcon.connect(HOST, PORT)  # Connect to brickd
        # Don't use device before ipcon is connected

