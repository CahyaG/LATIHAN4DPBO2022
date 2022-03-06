from Job import Job
from Person import Person

# multiple inheritance
class Driver(Person, Job):
    __licenseID = 0
    __activeUntil = "" # format dd-mm-yyyy
    __vehicleType = ""

    # contructor dibuat menjadi bisa langsung me-set class parent nya juga
    def __init__(self, NIK:int = 0, name:str = "", gender:str = "", NIP:int = 0, companyName:str = "", position:str = "", licenseID:int = 0, activeUntil:str = "", vehicleType:str = ""):
        # memanggil contructor parent
        Person.__init__(Person, NIK, name, gender)
        Job.__init__(Job, NIP, companyName, position)
        self.__licenseID = licenseID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    def getLicenseID(self) -> int:
        return self.__licenseID

    def setLicenseID(self, licenseID:int):
        self.__licenseID = licenseID

    def getActiveUntil(self) -> str:
        return self.__activeUntil

    def setActiveUntil(self, activeUntil:str):
        self.__activeUntil = activeUntil

    def getVehicleType(self) -> str:
        return self.__vehicleType

    def setVehicleType(self, vehicleType:str):
        self.__vehicleType = vehicleType

    # method untuk menampilkan data Driver
    def printDriver(self):
        print("license ID             : {}".format(self.__licenseID))
        print("Active Until           : {}".format(self.__activeUntil))
        print("Vehicle Type           : {}".format(self.__vehicleType))

    # method untuk menampilkan data Driver beserta data dari parent parent nya
    def printDriverDetail(self):
        self.printPerson()
        self.printJob()
        self.printDriver()