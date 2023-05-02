from Bricklets import Bricklets
from DataListener import DataListener
import resources as resc

class CommandHandler:
    def __init__(self, ipcon):
        if not resc.offlineMode:
            self.ipcon = ipcon
            self.Bricklets = Bricklets(ipcon)
            self.DataListener = DataListener()


    def evaluate(self, command):

        #Basic Commands
        if command == "help":
            print("Hilfe ist unterwegs")
        #elif command == "disconnect" or "exit":
        #   self.temperature_sensor.disconnect()


        # Commands for temperature_sensor:
        elif command == "get_temp":
            print(str(self.Bricklets.TemperatureSensor.get_temperature()) + "\n")
        else:
            return "Befehl unbekannt\n"