class Vehicle:
    __fuelType = ""
    __maxPassangers = 0
    __age = 0 # dalam tahun

    def __init__(self, fuelType:str = "", maxPassangers:int = 0, age:int = 0):
        self.__fuelType = fuelType
        self.__maxPassangers = maxPassangers
        self.__age = age

    def getFuelType(self) -> str:
        return self.__fuelType

    def setFuelType(self, fuelType:str):
        self.__fuelType = fuelType

    def getMaxPassangers(self) -> int:
        return self.__maxPassangers

    def setMaxPassangers(self, maxPassangers:int):
        self.__maxPassangers = maxPassangers

    def getAge(self) -> int:
        return self.__age
    
    def setAge(self, age:int):
        self.__age = age

    def Move(self, vehicle:str = "Vehicle"):
        print("{} is Moving".format(vehicle))

    def printVehicle(self):
        print("Fuel Type              : {}".format(self.__fuelType))
        print("Max Passangers         : {}".format(self.__maxPassangers))
        print("Age                    : {} years".format(self.__age))