class Job:
    __NIP = 0
    __companyName = ""
    __position = ""

    def __init__(self, NIP:int = 0, companyName:str = "", position:str = ""):
        self.__NIP = NIP
        self.__companyName = companyName
        self.__position = position

    def getNIP(self) -> int:
        return self.__NIP

    def setNIP(self, NIP:int):
        self.__NIP = NIP

    def getCompanyName(self) -> str:
        return self.__companyName

    def setCompanyName(self, companyName:str):
        self.__companyName = companyName

    def getPosition(self) -> str:
        return self.__position

    def setPosition(self, position:str):
        self.__position = position

    # method untuk print data Job
    def printJob(self):
        print("NIP                    : {}".format(self.__NIP))
        print("Company Name           : {}".format(self.__companyName))
        print("Position               : {}".format(self.__position))