from resources.texts import logo
from serverueberwachung.console_management.CommandHandler import CommandHandler
from serverueberwachung.console_management.Command_List import item_index, command_list
from serverueberwachung.resources.uid_list import HOST, PORT


# the user input the network configuration for connecting to the tinkerforge-server
def bootup():
    config_finished = False
    global HOST
    global PORT

    # try:
    #     while not config_finished:
    #         if HOST == "":
    #             HOST = input("Bitte geben sie die IP/Domain der Serverüberwachung ein: ")
    #         elif PORT == 0:
    #             PORT = int(input("Bitte geben sie den passenden Port ein: "))
    #         else:
    #             config_finished = True
    # except:
    #     print("keine Verbindung")


# beginning of the main loop
running = True
print(logo)
commandHandler = CommandHandler()

bootup()

# the main-loop of the programm
while running:
    command = input("=> ")
    if command.lower() == "exit":
        running = False
    else:
        commandHandler.evaluate(command.lower())
