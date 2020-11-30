
class Company:
    ID = ''
    password = ''
    companyname = ''
    email = ''
    address = ''
    annualsale = -1
    web = ''
    manager_name = ''
    manager_ph = ''
    introduce = ''
    major = ''
    pfauthority = ''
    pfperiod = ''
    request_authority = ''
    def __str__(self):
        print("id:" + self.ID)
        print("password:" + self.password)
        print("companyname:" + self.companyname)
        print("email:" + self.email)
        print("address:" + self.address)
        print("annualsale:" + self.annualsale)
        print("web:" + self.web)
        print("manager_name:" + self.manager_name)
        print("manager_ph:" + self.manager_ph)
        print("introduce:" + self.introduce)
        print("major:" + self.major)
        print("pfauthority:" + self.pfauthority)
        print("pfperiod:" + self.pfperiod)
        print("request_authority:" + self.request_authority)
