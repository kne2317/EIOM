import StudentDB
import pymysql
from Student import Student

def studentLogin(id,pw):
    student=Student()

    conn = pymysql.connect(host='localhost', user='eiom', password='1111', db='eiom_db', charset='utf8')
    curs = conn.cursor()

    sql = "select * from student where ID = '"+id+"';"
    curs.execute(sql)

    rows = curs.fetchall()
    if len(rows) > 0:
        if rows[0][1] == pw:
            student.setID(rows[0][0])
            student.setPassword(rows[0][1])
            return True
        else:
            return False
    else:
        return False

    conn.close()

def teacherLogin(id,pw):
    conn = pymysql.connect(host='localhost', user='eiom', password='1111', db='eiom_db', charset='utf8')
    curs = conn.cursor()

    conn.close()

def companyLogin(id,pw):
    conn = pymysql.connect(host='localhost', user='eiom', password='1111', db='eiom_db', charset='utf8')
    curs = conn.cursor()




    conn.close()
