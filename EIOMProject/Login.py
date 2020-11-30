
import pymysql

from BasicInfo import BasicDB
from student.Student import Student
from company.Company import Company
from teacher.Teacher import Teacher

def studentLogin(id,pw):

    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "select * from student where id = '"+id+"';"
    curs.execute(sql)

    rows = curs.fetchall()
    if len(rows) > 0:
        if rows[0][1] == pw:
            Student.ID=rows[0][0]
            Student.password = rows[0][1]
            Student.name = rows[0][2]
            Student.major = rows[0][3]
            Student.grade = rows[0][4]
            Student.class_ = rows[0][5]
            Student.portfolio = rows[0][6]
            Student.introduce = rows[0][7]
            Student.likeCompany = rows[0][8]
            Student.email = rows[0][9]

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
            Teacher.ID=rows[0][0]
            Teacher.name=rows[0][1]
            Teacher.password=rows[0][2]
            Teacher.email=rows[0][3]
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

    row = curs.fetchall()
    if len(row) > 0:
        if row[0][2] == pw:
            Company.companyname=row[0][0]
            Company.ID=row[0][1]
            Company.password=row[0][2]
            Company.address=row[0][3]
            Company.annualsales=row[0][4]
            Company.web=row[0][5]
            Company.email=row[0][6]
            Company.manager_name=row[0][7]
            Company.manager_ph=row[0][8]
            Company.introduce=row[0][9]
            Company.major=row[0][10]
            Company.pfauthority=row[0][11]
            Company.pfperiod=row[0][12]
            Company.request_authority=row[0][13]
            return True
        else:
            return False
    else:
        return False

    conn.close()
