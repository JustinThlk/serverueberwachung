from tinkerforge.ip_connection import IPConnection

import resources as resc

#
# References of all sensors
from tinkerforge.bricklet_ptc_v2 import BrickletPTCV2
from tinkerforge.bricklet_motion_detector_v2 import BrickletMotionDetectorV2
from tinkerforge.bricklet_ambient_light_v3 import BrickletAmbientLightV3
from tinkerforge.bricklet_humidity_v2 import BrickletHumidityV2
# References to all actors
from tinkerforge.bricklet_rgb_led_button import BrickletRGBLEDButton
from tinkerforge.bricklet_dual_button_v2 import BrickletDualButtonV2
from tinkerforge.bricklet_piezo_speaker_v2 import PiezoSpeakerV2
from tinkerforge.bricklet_segment_display_4x7_v2 import SegmentDisplay4x7V2
from tinkerforge.bricklet_e_paper_296x128 import EPaper296x128

class Bricklets:
    def __init__(self):
        ipcon = IPConnection()
        self.TemperatureSensor = BrickletPTCV2(resc.uid_list["tempsensor"], ipcon)
        self.MotionDetector = BrickletMotionDetectorV2(resc.uid_list["motiondetector"], ipcon)
        self.LightSensor = BrickletAmbientLightV3(resc.uid_list["ambientlight"], ipcon)
        self.HumiditySensor = BrickletHumidityV2(resc.uid_list["humidity"], ipcon)
        self.RGBButton = BrickletRGBLEDButton(resc.uid_list["rgbledbutton"], ipcon)
        self.DualButton = BrickletDualButtonV2(resc.uid_list["dualbutton"], ipcon)
        self.Speaker = PiezoSpeakerV2(resc.uid_list["piezo"], ipcon)
        self.SegmentDisplay = SegmentDisplay4x7V2(resc.uid_list["sevensegment"], ipcon)
        self.EPaperDisplay = EPaper296x128(resc.uid_list["epaper"], ipcon)
        ipcon.connect(resc.HOST, resc.PORT)
        # Don't use device before ipcon is connected
