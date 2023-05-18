from Bricklets import Bricklets
from DataListener import DataListener
from tabulate import tabulate
import resources as resc

class CommandHandler:
    def __init__(self):
        if not resc.offlineMode:
            self.Bricklets = Bricklets()
        self.Bricklets.RGBButton.register_callback(self.Bricklets.RGBButton.CALLBACK_BUTTON_STATE_CHANGED, button_pressed())
            #self.DataListener = DataListener()

    def button_pressed(self):
        if self.Bricklets.RGBButton.BUTTON_REFRESH:
            # Refresh the screen and read the current sensor values
            self.evaluate(command="display_status")

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

        #Commands for Actors/Sensors
        elif command == "set_colour":
            R_value = input("Wert für Rot(0-255): ")
            G_value = input("Wert für Grün(0-255): ")
            B_value = input("Wert für Blau(0-255): ")
            self.Bricklets.RGBButton.set_color(R_value, G_value, B_value)

        #Commands for Displays
        elif command == "display_status":
            def update_epaper_display(epaper):
                self.Bricklets.EPaperDisplay.clear_display()
                temperature = self.Bricklets.TemperatureSensor.get_temperature() / 100.0
                humidity = self.Bricklets.HumiditySensor.get_humidity() / 10.0
                illuminance = self.Bricklets.LightSensor.get_illuminance() / 10.0
                motion = self.Bricklets.MotionDetector.get_motion_detected()
                text = f"Temperature: {temperature} °C\n"
                text += f"Humidity: {humidity} %RH\n"
                text += f"Illuminance: {illuminance} lx\n"
                text += f"Motion: {'Detected' if motion else 'Not Detected'}"

                # Write the sensor values to the E-Paper display and updates the screen
                epaper.write_line(0, 0, text)
                epaper.draw()


        else:
            return "Befehl unbekannt\n"