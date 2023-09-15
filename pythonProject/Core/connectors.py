from dataclasses import dataclass

@dataclass
class Connector:
    @abtractmethod
    def getConnector(self):
        pass

class DbConnector(Connector):
    def getConnector(self):
        return "DbConnector"

