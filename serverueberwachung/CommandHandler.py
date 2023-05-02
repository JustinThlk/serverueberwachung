from Bricklets import Bricklets
from DataListener import DataListener
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
            print(str(self.Bricklets.TemperatureSensor.get_temperature() / 100.0) + " Grad Celsius\n")
            print(str(self.Bricklets.HumiditySensor.get_humidity() / 100.0) + "% Luftfeuchtigkeit\n")
            if self.Bricklets.MotionDetector.get_motion_detected() == 1:
                print("Bewegung erkannt\n")
            else:
                print("Keine Bewegung erkannt\n")
            print(str(self.Bricklets.LightSensor.get_illuminance() / 100.0) + " lx")
        elif command == "set_colour":
            R_value = input("Wert für Rot(0-255): ")
            G_value = input("Wert für Grün(0-255): ")
            B_value = input("Wert für Blau(0-255): ")
            self.Bricklets.RGBButton.set_color(R_value, G_value, B_value)
        else:
            return "Befehl unbekannt\n"