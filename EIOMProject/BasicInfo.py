import pymysql



class BasicInfo:
    def __init__(self):
        self.WindowWidth = 1200
        self.WindowHeight = 700
        self.WindowX = 400
        self.WindowY = 100
        #self.titleFont = 'Candara'
        self.titleFont = 'impact'
        self.font1 = '맑은 고딕'


class BasicDB:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='eiom', password='1111', db='eiom_db', charset='utf8')
