
class Teacher:
    def __init__(self):
        self.__ID = ''
        self.__password = ''
        self.__name = ''
        self.__email = ''

    def getID(self):
        return self.__ID
    def getPassword(self):
        return self.__password
    def getEmail(self):
        return self.__email
    def getName(self):
        return self.__name

    def setID(self, id):
        self.__ID = id
    def setPassword(self, password):
        self.__password = password
    def setEmail(self, email):
        self.__email = email
    def setName(self, name):
        self.__name = name

    def print(self):
        print("id : " + self.getID())
        print("password : " + self.getPassword())
        print("email : " + self.getEmail())
        print("name : " + self.getName())
