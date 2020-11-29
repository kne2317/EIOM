
class Student:
    def __init__(self):
        self.__ID = ''
        self.__password = ''
        self.__name = ''
        self.__email = ''
        self.__major = ''
        self.__grade = -1
        self.__class = -1
        self.__portfolio = ''
        self.__introduce = ''
        self.__likeCompany = ''


    def getID(self):
        return self.__ID
    def getPassword(self):
        return self.__password
    def getEmail(self):
        return self.__email
    def getName(self):
        return self.__name
    def getMajor(self):
        return self.__major
    def getGrade(self):
        return self.__grade
    def getClass(self):
        return self.__class
    def getPortfolio(self):
        return self.__portfolio
    def getIntroduce(self):
        return self.__introduce
    def getLikeCompany(self):
        return self.__likeCompany

    def setID(self, id):
        self.__ID = id
    def setPassword(self, password):
        self.__password = password
    def setEmail(self, email):
        self.__email = email
    def setName(self, name):
        self.__name = name
    def setMajor(self, major):
        self.__major = major
    def setGrade(self, grade):
        self.__grade = grade
    def setClass(self, Class):
        self.__class = Class
    def setPortfolio(self, portfolio):
        self.__portfolio = portfolio
    def setIntroduce(self, introduce):
        self.__introduce = introduce
    def setLikeCompany(self, likeCompany):
        self.__likeCompany = likeCompany

    def print(self):
        print("id : " + self.getID())
        print("password : " + self.getPassword())
        print("email : " + self.getEmail())
        print("name : " + self.getName())
        print("major : " + self.getMajor())
        print("grade : " + (str)(self.getGrade()))
        print("class : " + (str)(self.getClass()))
        print("portfolio : " + self.getPortfolio())
        print("introduce : " + self.getIntroduce())
        print("likeCompany : " + self.getLikeCompany())
