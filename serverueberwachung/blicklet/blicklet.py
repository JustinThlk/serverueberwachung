from abc import ABC, abstractmethod
class bricklet(ABC):

    @abstractmethod
    def setup(self):
        pass