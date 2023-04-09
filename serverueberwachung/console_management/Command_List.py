command_list = (
    "show_data",
    "econfig",
    "h_temp",
    "h_move",
    "h_wet",
    "h_ligth",
    "l_temp",
    "l_move",
    "l_wet",
    "l_ligth",
    "g_temp",
    "exit",
    "g_motion",
    "g_humidity",
    "g_light",
)


def item_index(command):
    pos = command_list.index(command)
    return command_list[pos]
