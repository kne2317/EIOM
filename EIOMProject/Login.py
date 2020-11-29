
import pymysql

from BasicInfo import BasicDB
from student.Student import Student


def studentLogin(id,pw):
    student=Student()

    basicDB = BasicDB()
    conn = basicDB.conn
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
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    conn.close()

def companyLogin(id,pw):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()




    conn.close()
