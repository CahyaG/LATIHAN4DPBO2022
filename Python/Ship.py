from Vehicle import Vehicle
from Driver import Driver

class Ship(Vehicle):
    __type = ""
    __countryOfManufacture = ""
    __nahkoda = Driver()
    
    # contructor dibuat menjadi bisa langsung me-set class parent nya juga
    def __init__(self, fuelType:str = "", maxPassangers:int = 0, age:int = 0, type:str = "", countryOfManufacture:str = "", nahkoda:Driver = Driver()):
        # memanggil constructor parent
        super().__init__(fuelType, maxPassangers, age)
        self.__type = type
        self.__countryOfManufacture = countryOfManufacture
        self.__nahkoda = nahkoda

    def getType(self) -> str:
        return self.__type

    def setType(self, type:str):
        self.__type = type

    def getCountryOfManufacture(self) -> str:
        return self.__countryOfManufacture

    def setCountryOfManufacture(self, countryOfManufacture:str):
        self.__countryOfManufacture = countryOfManufacture

    def getNahkoda(self) -> Driver:
        return self.__nahkoda

    def setNahkoda(self, nahkoda:Driver):
        self.__nahkoda = nahkoda


    # memanggil method Move dari class parent dengan argument "Ship"
    def Move(self):
        super().Move("Ship")

    # method untuk menampilkan data ship
    def printShip(self):
        print("Type                   : {}".format(self.__type))
        print("Country Of Manufacture : {}".format(self.__countryOfManufacture))
        # print data nahkoda yang merupakan object dari kelas Driver
        print("------------------------Nahkoda------------------------")
        self.__nahkoda.printDriverDetail()
        print("-------------------------------------------------------")
        self.Move()

    # method untuk menampilkan data ship beserta data dari parent nya yaitu Vehicle
    def printShipDetail(self):
        self.printVehicle()
        self.printShip()
    