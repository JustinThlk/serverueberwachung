import blicklet
import config
import console_management
import resources
import source


running = True
while (running):
    print()
    command = input("=> ")

    if command == "exit":
        running = False
    elif command.lower() == "hallo":
        print("Hallo wie geht es ihnen?\n")
    else:
        print("Befehl unbekannt\n")