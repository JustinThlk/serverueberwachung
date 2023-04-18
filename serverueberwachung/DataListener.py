from Bricklets import Bricklets

def saveHumidity(humidity):
    print(humidity / 100.0)


class DataListener:

    def __init__(self):
        self.Bricklets = Bricklets()
        self.listening = True

    def start(self):
        while self.listening:
            self.Bricklets.HumiditySensor.register_callback(self.Bricklets.HumiditySensor.CALLBACK_HUMIDITY, saveHumidity)
