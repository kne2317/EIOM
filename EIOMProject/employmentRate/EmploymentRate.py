from BasicInfo import BasicDB


class ERate:
    def __init__(self):
        self.__year=''
        self.__grade3=-1
        self.__eiom=-1
        self.__self=-1
        self.__scene=-1
        self.__request_cnt=-1

    def getYear(self):
        return self.__year
    def getGrade3(self):
        return self.__grade3
    def getEiom(self):
        return self.__eiom
    def getSelf(self):
        return self.__self
    def getScene(self):
        return self.__scene
    def getRequest_cnt(self):
        return self.__request_cnt

    def setYear(self,y):
        self.__year=y
    def setGrade3(self,g):
        self.__grade3=g
    def setEiom(self,e):
        self.__eiom=e
    def setSelf(self,s):
        self.__self=s
    def setScene(self,s):
        self.__scene=s
    def setRequest_cnt(self,r):
        self.__request_cnt=r



def eRateDB(i):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "select * from employee_rate ORDER BY year DESC LIMIT 3;"
    curs.execute(sql)

    rows = curs.fetchall()

    y1 = {'year': rows[0][0], 'grade3': rows[0][1], 'eiom': rows[0][2], 'self': rows[0][3], 'scene': rows[0][4],'request_cnt': rows[0][5]}
    y2 = {'year': rows[1][0], 'grade3': rows[1][1], 'eiom': rows[1][2], 'self': rows[1][3], 'scene': rows[1][4],'request_cnt': rows[1][5]}
    y3 = {'year': rows[2][0], 'grade3': rows[2][1], 'eiom': rows[2][2], 'self': rows[2][3], 'scene': rows[2][4],'request_cnt': rows[2][5]}

    if i==1: return y1
    if i==2: return y2
    if i==3: return y3

def employRate(total, employed):
    return employed/total*100

def updateRate(y1,y2,y3):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "update employee_rate set grade3_people_num = "+str(y1['grade3'])+", eiom="+str(y1['eiom'])+\
          ", self="+str(y1['self'])+", scene="+str(y1['scene'])+", request_cnt="+str(y1['request_cnt'])+" where year='"+y1['year']+"';"
    curs.execute(sql)
    conn.commit()

    sql = "update employee_rate set grade3_people_num = " + str(y2['grade3']) + ", eiom=" + str(y2['eiom']) + \
          ", self=" + str(y2['self']) + ", scene=" + str(y2['scene']) + ", request_cnt=" + str(y2['request_cnt']) + " where year='"+y2['year']+"';"
    curs.execute(sql)
    conn.commit()

    sql = "update employee_rate set grade3_people_num = " + str(y3['grade3']) + ", eiom=" + str(y3['eiom']) + \
          ", self=" + str(y3['self']) + ", scene=" + str(y3['scene']) + ", request_cnt=" + str(y3['request_cnt']) + " where year='"+y3['year']+"';"
    curs.execute(sql)
    conn.commit()

    print("업데이트")