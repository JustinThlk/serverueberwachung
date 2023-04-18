from serverueberwachung.bricklet.sensors import Temperature, Humidity, MotionDetector, AmbientLight
from serverueberwachung.console_management.Command_List import item_index, command_list
from serverueberwachung.console_management.Main_Menu import init_menu, save_selected_option

class CommandHandler:

    def __init__(self):
        self.temperature_sensor = Temperature.temp_sensor()


    def evaluate(self, command):

        #Basic Commands
        if command == "help":
            print("Hilfe ist unterwegs")
        elif command == "disconnect" or "exit":
            self.temperature_sensor.disconnect()


        # Commands for temperature_sensor:
        elif command == "get_temp":
            print(self.temperature_sensor.get_temp() + "\n")
        else:
            return "Befehl unbekannt\n"



    # elif command == item_index("g_temp"): #todo for testing only
    #     print(Temperature.get_temp())
    # elif command == item_index("g_motion"): #todo for testing only
    #     print(MotionDetector.get_motion())
    # elif command == item_index("g_humidity"):  # todo for testing only
    #     print(Humidity.get_humidity())
    # elif command == item_index("g_light"):  # todo for testing only
    #     print(AmbientLight.get_ligth())
    # elif command == "test":
    #     print("test")
    #     print(Temperature.is_connected())
    #
    # elif command == item_index("show_data"):
    #     tmp = item_index("show_data")
    #     print(tmp)
    # elif command == item_index("econfig"):
    #     tmp = item_index("econfig")
    #     print(tmp)
    # elif command == item_index("h_temp"):
    #     tmp = item_index("h_temp")
    #     print(tmp)
    # elif command == item_index("h_move"):
    #     tmp = item_index("h_move")
    #     print(tmp)