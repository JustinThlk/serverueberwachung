import resources as resc
from CommandHandler import CommandHandler
from tinkerforge.ip_connection import IPConnection

# the user input the network configuration for connecting to the tinkerforge-server
running = True
def bootup():
    global running
    config_finished = False
    while not config_finished:
        offline_mode = input("Möchten sie sich verbinden? [j/N]: ").lower()

        if offline_mode == ("j" or "y" or "ja" or "yes"):
            resc.HOST = input("Bitte geben sie die IP/Domain der Serverüberwachung ein: ")
            resc.PORT = int(input("Bitte geben sie den passenden Port ein: "))
            try:
                ipcon.connect(resc.HOST, resc.PORT)
            except:
                print("Verbindung konnte nicht aufgebaut werden\n")
            if ipcon.get_connection_state() == 1:
                config_finished = True

        elif offline_mode == ("n" or "nein" or "no"):
            print("offline")
            resc.offlineMode = True
            config_finished = True
            #todo: OfflineModus muss oder kann Implementiert werden

        elif offline_mode == ("exit" or "beenden"  or "close"):
            config_finished = True
            running = False

        else:
            print("Ungültige Eingabe!\n")


# beginning of the main loop
ipcon = IPConnection() # Create IP connection
print(resc.logo)

#initializes first bootup
bootup()

#creats commandhandler
commandHandler = CommandHandler(ipcon)

# the main-loop of the programm
while running:
    command = input("=> ")
    if command.lower() == "exit":
        running = False
    else:
        commandHandler.evaluate(command.lower())
