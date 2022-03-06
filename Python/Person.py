class Person:
    __NIK = 0
    __name = ""
    __gender = ""

    def __init__(self, NIK:int = 0, name:str = "", gender:str = ""):
        self.__NIK = NIK
        self.__name = name
        self.__gender = gender

    def getNIK(self) -> int:
        return self.__NIK

    def setNIK(self, NIK:int):
        self.__NIK = NIK

    def getName(self) ->str:
        return self.__name

    def setName(self, name:str):
        self.__name = name

    def getGender(self) -> str:
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender

    def sleep(self):
        print("{} is Sleeping".format(self.__name))

    ## method untuk menampilkan data Person
    def printPerson(self):
        print("NIK                    : {}".format(self.__NIK))
        print("Name                   : {}".format(self.__name))
        print("Gender                 : {}".format(self.__gender))
        self.sleep()
