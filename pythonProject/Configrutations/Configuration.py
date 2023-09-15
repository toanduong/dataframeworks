from abc import ABC, abstractmethod

class IConfiguration(ABC):
    @abstractmethod
    def getConfig(self):
        pass
