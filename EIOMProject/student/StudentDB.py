
import pymysql
from BasicInfo import BasicDB
from student.Student import Student

def getLanguages():
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "DESCRIBE languages;"
    curs.execute(sql)
    rows1 = curs.fetchall()

    languages = []
    for i in range(1, len(rows1)):
        languages.append(rows1[i][0])

    return languages


def updateStudentInfo(name, major, grade, class_,likecompany,pf,intro):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql="update student set name='"+name+"';"