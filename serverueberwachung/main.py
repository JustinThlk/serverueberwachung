from resources.texts import logo
import serverueberwachung.console_management.CommandHandler as CommandHandler
from serverueberwachung.console_management.Command_List import item_index, command_list
from serverueberwachung.resources.uid_list import HOST, PORT


# the user input the network configuration for connecting to the tinkerforge-server
def bootup():
    config_finished = False
    global HOST
    global PORT

    try:
        while not config_finished:
            if HOST == "":
                HOST = input("Bitte geben sie die IP/Domain der Serverüberwachung ein: ")
            elif PORT == "":\
                PORT = input("Bitte geben sie den passenden Port ein: ")
            else:
                config_finished = True
    except:
        print("keine Verbindung")


# beginning of the main loop
running = True
print(logo)

bootup()

# the main-loop of the programm
while running:
    command = input("=> ")
    try:
        if command.lower() == item_index("exit"):
            HOST = ""
            PORT = ""
            running = False
        else:
           print(CommandHandler.evaluate(CommandHandler, command.lower()))
    except:
        print("Value Error")

