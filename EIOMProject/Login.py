
import pymysql

from BasicInfo import BasicDB
from student.Student import Student
from company.Company import Company


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

    company=Company()

    sql = "select * from company where id = '" + id + "';"
    curs.execute(sql)

    row = curs.fetchall()
    if len(row) > 0:
        if row[0][2] == pw:
            company.companyname=row[0][0]
            company.id=row[0][1]
            company.password=row[0][2]
            company.address=row[0][3]
            company.annualsales=row[0][4]
            company.web=row[0][5]
            company.email=row[0][6]
            company.managername=row[0][7]
            company.managerph=row[0][8]
            company.introduce=row[0][9]
            company.major=row[0][10]
            company.pfauthority=row[0][11]
            company.pfperiod=row[0][12]
            company.request_authority=row[0][13]
            return True
        else:
            return False
    else:
        return False

    conn.close()
