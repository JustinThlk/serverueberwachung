from resources.texts import logo
from resources.uid_list import HOST, PORT
import console_management.CommandHandler as CommandHandler

# the user input the network configuration for connecting to the tinkerforge-server
def bootup():
    config_finished = False
    global HOST
    global PORT
    while not config_finished:
        HOST = input("Bitte geben sie die IP/Domain der Serverüberwachung ein: ")
        PORT = int(input("Bitte geben sie den passenden Port ein: ")) # PORT als Typecast int, da sonst nicht kompatibel mit Tinkerforge-Packages
        if HOST != "" and PORT != "":
            config_finished = True

# beginning of the main loop
running = True
print(logo)


bootup()

# the main-loop of the programm
while running:
    command = input("=> ")
    if command.lower() == "exit":
        running = False
    else:
        print(CommandHandler.evaluate(CommandHandler, command.lower()))
