from Bricklets import Bricklets
from DataListener import DataListener
from tabulate import tabulate
import resources as resc

class CommandHandler:
    def __init__(self):
        if not resc.offlineMode:
            self.Bricklets = Bricklets()
            #self.DataListener = DataListener()


    def evaluate(self, command):

        #Basic Commands
        if command == "help":
            print("Hilfe ist unterwegs")
        elif command == "open the pod bay doors hal":
            print("I'm sorry, Dave. I'm afraid I can't do that.")
        elif command == "beam me up scotty":
            print("Roger Roger")
        elif command == ("luke i am your father" or "i am your father"):
            print("No, it can't be!")

        # Commands for temperature_sensor:
        elif command == "get_temp":
            print(str(self.Bricklets.TemperatureSensor.get_temperature()/100.0) + " Grad Celsius\n")
        elif command == "get_humidity":
            print(str(str(self.Bricklets.HumiditySensor.get_humidity()/100.0) + "% Luftfeuchtigkeit\n"))
        elif command == "detect_motion":
            if self.Bricklets.MotionDetector.get_motion_detected() == 1:
                print("Bewegung erkannt\n")
            else:
                print("Keine Bewegung erkannt\n")
        elif command == "get_light":
            print(str(self.Bricklets.LightSensor.get_illuminance()/100.0) + " lx")
        elif command == "status":
            temp_temperature = self.Bricklets.TemperatureSensor.get_temperature() / 100.0
            temp_humidity = self.Bricklets.HumiditySensor.get_humidity() / 100.0
            if self.Bricklets.MotionDetector.get_motion_detected() == 1:
                temp_motion = "Bewegung erkannt"
            else:
                temp_motion = "Keine Bewegung erkannt"
            temp_light = self.Bricklets.LightSensor.get_illuminance() / 100.0
            # Used tabulate for this: https://pypi.org/project/tabulate/
            print(tabulate([['Temperatur', temp_temperature],
                            ['Feuchtigkeit', temp_humidity],
                            ['Bewegungsmelder', temp_motion],
                            ['Helligkeit', temp_light]],
                           headers=['Sensor', 'Wert'],
                           tablefmt="rounded_outline"))
        elif command == "set_colour":
            R_value = input("Wert für Rot(0-255): ")
            G_value = input("Wert für Grün(0-255): ")
            B_value = input("Wert für Blau(0-255): ")
            self.Bricklets.RGBButton.set_color(R_value, G_value, B_value)
        else:
            return "Befehl unbekannt\n"