from consolemenu import ConsoleMenu
from consolemenu.items import SubmenuItem, CommandItem
from serverueberwachung.console_management.Command_List import command_list, item_index

main_menu = ConsoleMenu("Haupt-Menu")
history_menu = ConsoleMenu("Historie aller Messwerte")
limit_menu = ConsoleMenu("Grenzwerte setzen")

def init_menu(): # Todo commands to execute
    main_menu.clear_screen()
    #main_menu items
    current_Data = CommandItem("aktuelle Messwerte anzeigen", item_index("show_data"))
    history_Data = SubmenuItem("Messwert Historie", history_menu, menu=main_menu)
    limit_sensor = SubmenuItem("Grenzwerte setzen", limit_menu, menu=main_menu)
    email_configuration = CommandItem("E-Mail Konfiguration", item_index("econfig"))

    #history menu items
    h_temperature = CommandItem("Termperatursensor", item_index("h_temp"))
    h_move = CommandItem("Bewegungssensor", item_index("h_move"))
    h_light = CommandItem("Helligkeitssensor", item_index("h_ligth"))
    h_wet = CommandItem("Feuchtigkeitssensor", item_index("h_wet"))

    #limit menu items
    l_temperature = CommandItem("Termperatursensor", item_index("l_temp"))
    l_move = CommandItem("Bewegungssensor", item_index("l_move"))
    l_light = CommandItem("Helligkeitssensor", item_index("l_ligth"))
    l_wet = CommandItem("Feuchtigkeitssensor", item_index("l_wet"))

    #append to main menu
    main_menu.append_item(current_Data)
    main_menu.append_item(history_Data)
    main_menu.append_item(limit_sensor)
    main_menu.append_item(email_configuration)

    #append to history menu
    history_menu.append_item(h_temperature)
    history_menu.append_item(h_move)
    history_menu.append_item(h_light)
    history_menu.append_item(h_wet)

    #append to limit menu
    limit_menu.append_item(l_temperature)
    limit_menu.append_item(l_move)
    limit_menu.append_item(l_light)
    limit_menu.append_item(l_wet)
    main_menu.show()

def save_selected_option():

    print("input" + str(main_menu.get_input())) #todo combine commands from list with menu commands the same :)

