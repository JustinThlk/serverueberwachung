from serverueberwachung.resources.uid_list import HOST, PORT
from serverueberwachung.blicklet.sensors import Temperature, Humidity, MotionDetector, AmbientLight
def initialize_bricklets():
    temperature_sensor = Temperature


def evaluate(self, command):
    if command == "hallo":
        return "Hallo wie geht es ihnen?\n"
    elif command == "temperaturlesen":
        print(temperature_sensor.getTemp())
    else:
        return "Befehl unbekannt\n"