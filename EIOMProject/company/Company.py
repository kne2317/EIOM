
class Company:
    def __init__(self):
        self.__ID = ''
        self.__password = ''
        self.__companyname = ''
        self.__email = ''
        self.__address = ''
        self.__annualsale = -1
        self.__web = ''
        self.__manager_name = ''
        self.__manager_ph = ''
        self.__introduce = ''
        self.__major = ''
        self.__pfauthority = ''
        self.__pfperiod = ''
        self.__request_authority = ''


    def getID(self):
        return self.__ID

    def getPassword(self):
        return self.__password

    def getCompanyname(self):
        return self.__companyname

    def getEmail(self):
        return self.__email

    def getAddress(self):
        return self.__address

    def getAnnualsale(self):
        return self.__annualsale

    def getWeb(self):
        return self.__web

    def getManager_name(self):
        return self.__manager_name

    def getManager_ph(self):
        return self.__manager_ph

    def getIntroduce(self):
        return self.__introduce

    def getMajor(self):
        return self.__major

    def getPfauthority(self):
        return self.__pfauthority

    def getPfperiod(self):
        return self.__pfperiod

    def getRequest_authority(self):
        return self.__request_authority


    def setID(self, id):
        self.__ID = id

    def setPassword(self, password):
        self.__password = password

    def setCompanyname(self, name):
        self.__companyname = name

    def setEmail(self, mail):
        self.__email = mail

    def setAddress(self, address):
        self.__address = address

    def setAnnualsale(self, sale):
        self.__annualsale = sale

    def setWeb(self, web):
        self.__web = web

    def setManager_name(self, mname):
        self.__manager_name = mname

    def setManager_ph(self, mph):
        self.__manager_ph = mph

    def setIntroduce(self, introduce):
        self.__introduce = introduce

    def setMajor(self, major):
        self.__major = major

    def setPfauthority(self, pfauthority):
        self.__pfauthority = pfauthority

    def setPfperiod(self, pfperiod):
        self.__pfperiod = pfperiod

    def setRequest_authority(self, reque):
        self.__request_authority = reque