class Birth:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def setYear(self, year):
        self.year = year

    def setMonth(self, month):
        self.month = month

    def setDay(self, day):
        self.day = day

class Student:
    def __init__(self):
        self.__ID = ''
        self.__password = ''
        self.__name = ''
        self.__birth = Birth(0, 0, 0)
        self.__portfolio = ''
        self.__useLanguage = []
        self.__likeCompany = []

    def printStudent(self):
        print("이름: ", end="")
        print(self.getName())
        print("아이디: ", end="")
        print(self.getID())
        print("비밀번호: ", end="")
        print(self.getPassword())
        print("생년월일: ", end="")
        print(self.getBirth().year, end="-")
        print(self.getBirth().month, end="-")
        print(self.getBirth().day)
        print("사용언어: ", end="")
        print(self.getUseLanguage())
        print("관심회사: ", end="")
        print(self.getLikeCompany())


    def setStudent(self, id, password, name, birth_year, birth_month, birth_day, portfolio, useLanguage, likeCompany):
        self.__ID = id
        self.__password = password
        self.__name = name
        self.__birth.year = birth_year
        self.__birth.month = birth_month
        self.__birth.day = birth_day
        self.__portfolio = portfolio
        self.__useLanguage = useLanguage
        self.__likeCompany = likeCompany

    def setID(self, ID):
        self.__ID = ID

    def getID(self):
        return self.__ID

    def setPassword(self, password):
        self.__password = password

    def getPassword(self):
        return self.__password

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setBirth(self, birth_year, birth_month, birth_day):
        self.__birth.setYear(birth_year)
        self.__birth.setMonth(birth_month)
        self.__birth.setDay(birth_day)

    def getBirth(self):
        return self.__birth

    def addPortfolio(self, portfolio):
        pass


    def setUseLanguage(self, languageDict):
        self.__useLanguage = (languageDict)

    def getUseLanguage(self):
        return self.__useLanguage

    def addUseLanguage(self, language):
        self.__useLanguage.append(language)


    def setLikeCompany(self, companylist):
        self.__likeCompany = companylist

    def getLikeCompany(self):
        return self.__likeCompany

    def addLikeCompany(self, company):
        self.__likeCompany.append(company)