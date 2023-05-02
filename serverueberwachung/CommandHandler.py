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

        # Commands for temperature_sensor:
        elif command == "get_temp":
            print(str(self.Bricklets.TemperatureSensor.get_temperature()/100.0) + " Grad Celsius\n")
        else:
            return "Befehl unbekannt\n"