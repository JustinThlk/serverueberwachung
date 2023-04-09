from serverueberwachung.blicklet.sensors import Temperature, Humidity, MotionDetector, AmbientLight
from serverueberwachung.console_management.Command_List import item_index, command_list
from serverueberwachung.console_management.Main_Menu import init_menu, save_selected_option

def initialize_bricklets():
    temperature_sensor = Temperature
    motion_detector_sensor = MotionDetector
    humidity_sensor = Humidity
    ambient_light_sensor = AmbientLight

def evaluate(self, command): #todo add all commands
    if command.lower() == "":
        try:
            init_menu()
        except:
            print("error")

    elif command == item_index("g_temp"): #todo for testing only
        print(Temperature.get_temp())
    elif command == item_index("g_motion"): #todo for testing only
        print(MotionDetector.get_motion())
    elif command == item_index("g_humidity"):  # todo for testing only
        print(Humidity.get_humidity())
    elif command == item_index("g_light"):  # todo for testing only
        print(AmbientLight.get_ligth())

    elif command == item_index("show_data"):
        tmp = item_index("show_data")
        print(tmp)
    elif command == item_index("econfig"):
        tmp = item_index("econfig")
        print(tmp)
    elif command == item_index("h_temp"):
        tmp = item_index("h_temp")
        print(tmp)
    elif command == item_index("h_move"):
        tmp = item_index("h_move")
        print(tmp)
    else:
        return "Befehl unbekannt\n"