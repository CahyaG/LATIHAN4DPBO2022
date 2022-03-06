from tokenize import Double
from Vehicle import Vehicle
from Driver import Driver

class Airplane(Vehicle):
    __type = ""
    __wingsLength = 0 # dalam meter
    __pilot = Driver()
    __coPilot = Driver()
    
    # contructor dibuat menjadi bisa langsung me-set class parent nya juga
    def __init__(self, fuelType:str = "", maxPassangers:int = 0, age:int = 0, type:str = "", wingsLength:float = 0, pilot:Driver = Driver(), coPilot:Driver = Driver()):
        # memanggil contructor parent
        super().__init__(fuelType, maxPassangers, age)
        self.__type = type
        self.__wingsLength = wingsLength
        self.__pilot = pilot
        self.__coPilot = coPilot

    def getType(self) -> str:
        return self.__type

    def setType(self, type:str):
        self.__type = type

    def getWingsLength(self) -> float:
        return self.__wingsLength
    
    def setWingsLength(self, wingsLength:float):
        self.__wingsLength = wingsLength

    def getPilot(self) -> Driver:
        return self.__pilot

    def setPilot(self, pilot:Driver):
        self.__pilot = pilot

    def getCoPilot(self) -> Driver:
        return self.__coPilot

    def setCoPilot(self, coPilot:Driver):
        self.__coPilot = coPilot

    # memanggil method Move dari class parent dengan argument "Airplane"
    def Move(self):
        super().Move("Airplane")

    # methos untuk menampilkan data Airplane
    def printAirplane(self):
        print("Type                   : {}".format(self.__type))
        print("Wings Length           : {}m".format(self.__wingsLength))
        print("-----------------------Pilot---------------------------")
        self.__pilot.printDriverDetail()
        print("-------------------------------------------------------")
        print("---------------------Co-Pilot--------------------------")
        self.__coPilot.printDriverDetail()
        print("-------------------------------------------------------")
        self.Move()

    # method untuk menampilkan data airplane beserta data dari parentnya
    def printAirplaneDetail(self):
        self.printVehicle()
        self.printAirplane()
        