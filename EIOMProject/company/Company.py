class Company:
    def __init__(self):
        self.__ID = ''
        self.__password = ''
        self.__companyname = ''
        self.__email = ''
        self.__major = ''
        self.__address = ''
        self.__annualsales = ''
        self.__introduce = ''
        self.__managername = ''
        self.__managerph = ''
        self.__pfauthority = ''
        self.__pfperiod = ''
        self.__request_authority = ''

    def getPfauthority(self):
        return self.__pfauthority
    def getPfperiod(self):
        return self.__pfperiod
    def getID(self):
        return self.__ID
    def getPassword(self):
        return self.__password
    def getEmail(self):
        return self.__email
    def getCompanyname(self):
        return self.__companyname
    def getMajor(self):
        return self.__major
    def getAddress(self):
        return self.__address
    def getAnnualsales(self):
        return self.__annualsales
    def getRequest_authority(self):
        return self.__request_authority
    def getIntroduce(self):
        return self.__introduce
    def getManagerph(self):
        return self.__managerph
    def getManagername(self):
        return self.__managername

    def setPfauthority(self,pfauthority):
        self.__pfauthority=pfauthority

    def setPfperiod(self,pfperiod):
        self.__pfperiod=pfperiod

    def setID(self,id):
        self.__ID=id

    def setPassword(self,password):
        self.__password=password

    def setEmail(self,email):
        self.__email=email

    def setCompanyname(self,companyname):
        self.__companyname=companyname

    def setMajor(self,major):
        self.__major=major

    def setAddress(self,address):
        self.__address=address

    def setAnnualsales(self,annualsales):
        self.__annualsales=annualsales

    def setRequest_authority(self,request_authority):
        self.__request_authority=request_authority

    def setIntroduce(self,introduce):
        self.__introduce=introduce

    def setManagerph(self,managerph):
        self.__managerph=managerph

    def setManagername(self,managername):
        self.__managername=managername

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