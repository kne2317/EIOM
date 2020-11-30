
class Student:
    ID = ''
    password = ''
    name = ''
    email = ''
    major = ''
    grade = -1
    class_ = -1
    portfolio = ''
    introduce = ''
    likeCompany = ''
    def print(self):
        print("id: " + self.ID)
        print("password: " + self.password)
        print("name: " + self.name)
        print("email: " + self.email)
        print("major: " + self.major)
        print("grade: " + str(self.grade))
        print("class_: " + str(self.class_))
        print("portfolio: " + self.portfolio)
        print("introduce: " + self.introduce)
        print("likeCompany: " + self.likeCompany)

class Languages:
    def __init__(self):
        self.c = False
        self.cpp = False
        self.cs = False
        self.py = False
        self.html = False
        self.css = False
        self.js = False
        self.jq = False
        self.jsp = False
        self.php = False
        self.node = False
        self.react = False
        self.java = False
        self.spring = False
        self.servlet = False
        self.kotlin = False
        self.android = False
        self.linux = False
        self.oracle = False
        self.mysql = False
        self.etc = ''