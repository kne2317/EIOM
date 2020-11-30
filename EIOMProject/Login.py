
import pymysql

from BasicInfo import BasicDB
from student.Student import Student
from company.Company import Company
from teacher.Teacher import Teacher

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
            student.ID=rows[0][0]
            student.password[0][1]
            student.name[0][2]
            student.major[0][3]
            student.grade[0][4]
            student.class_[0][5]
            student.portfolio[0][6]
            student.introduce[0][7]
            student.likeCompany[0][8]
            student.email[0][9]

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

    teacher = Teacher()

    sql = "select * from teacher where id = '" + id + "';"
    curs.execute(sql)

    rows = curs.fetchall()
    if len(rows) > 0:
        print(rows)
        if rows[0][2] == pw:
            teacher.ID=rows[0][0]
            teacher.name=rows[0][1]
            teacher.password=rows[0][2]
            teacher.email=rows[0][3]
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
            company.ID=row[0][1]
            company.password=row[0][2]
            company.address=row[0][3]
            company.annualsales=row[0][4]
            company.web=row[0][5]
            company.email=row[0][6]
            company.manager_name=row[0][7]
            company.manager_ph=row[0][8]
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
