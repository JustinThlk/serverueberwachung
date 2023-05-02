from tinkerforge.ip_connection import IPConnection

#Configuration Variables
offlineMode = False


# list of Host and Port Configuration
HOST = "172.20.10.31"
PORT = 4223

#the ip connection object

# ipcon_Temperature = IPConnection()
# ipcon_MotionDetection = IPConnection()
# ipcon_LightSensor = IPConnection()
# ipcon_Humidity = IPConnection
# ipcon_RGB_Button  = IPConnection()
# ipcon_Dual_Button = IPConnection()
# ipcon_Piezo_Speaker = IPConnection()
# ipcon_E_Paper = IPConnection()
# ipcon_Segment_Display = IPConnection()

# list of UIDs for the tinkerforge bricklets
uid_list ={
"tempsensor" : "Wcg",
"ambientlight" : "Pdw",
"humidity" : "ViW",
"motiondetector" : "ML4",
"rgbledbutton" : "23Qx",
"dualbutton" : "Vd8",
"piezo" : "R7M",
"epaper" : "XGL",
"sevensegment" : "Tre",
}

# Bootup logo
logo = "  _______       __             ______                       __\n\
 /_  __(_)___  / /_____  _____/ ____/___  ____  _________  / /__\n\
  / / / / __ \/ //_/ _ \/ ___/ /   / __ \/ __ \/ ___/ __ \/ / _ \ \n\
 / / / / / / / ,< /  __/ /  / /___/ /_/ / / / (__  ) /_/ / /  __/\n\
/_/ /_/_/ /_/_/|_|\___/_/   \____/\____/_/ /_/____/\____/_/\___/"