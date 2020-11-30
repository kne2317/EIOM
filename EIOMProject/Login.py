
import pymysql

from BasicInfo import BasicDB
from student.Student import Student


def studentLogin(id,pw):
    student=Student()

    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "select * from student where id = '"+id+"';"
    curs.execute(sql)

    rows = curs.fetchall()
    if len(rows) > 0:
        if rows[0][1] == pw:

            student.setID(rows[0][0])
            student.setPassword(rows[0][1])
            student.setName(rows[0][2])
            student.setMajor(rows[0][3])
            student.setGrade(rows[0][4])
            student.setClass(rows[0][5])
            student.setPortfolio(rows[0][6])
            student.setIntroduce(rows[0][7])
            student.setLikeCompany(rows[0][7])
            student.setEmail(rows[0][8])

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

    sql = "select * from teacher where id = '" + id + "';"
    curs.execute(sql)

    rows = curs.fetchall()
    if len(rows) > 0:
        print(rows)
        if rows[0][2] == pw:

            return True
        else:
            return False
    else:
        return False

    conn.close()

def companyLogin(id,pw):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "select * from company where id = '" + id + "';"
    curs.execute(sql)

    rows = curs.fetchall()
    if len(rows) > 0:
        if rows[0][2] == pw:
            return True
        else:
            return False
    else:
        return False

    conn.close()
