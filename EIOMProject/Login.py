import pymysql
from Student import Student
import StudentDB


def studentLogin(student):
    conn = pymysql.connect(host='localhost', user='root', password='hi0310', db='eiom', charset='utf8')
    curs = conn.cursor()

    sql = "select * from student where ID like '"+student.getID()+"';"
    curs.execute(sql)

    rows1 = curs.fetchall()
    if len(rows1) > 0:
        student.setName(rows1[0][2])
        student.setBirth(rows1[0][3].year, rows1[0][3].month, rows1[0][3].day)
        if rows1[0][5] != None:
            student.setLikeCompany(rows1[0][5].split(';'))

        if rows1[0][1] == student.getPassword():
            sql = "select * from languages where ID like '"+student.getID()+"';"
            curs.execute(sql)

            rows2 = curs.fetchall()

            '''sql = "DESCRIBE languages;"
            curs.execute(sql)
            rows3 = curs.fetchall()

            languages = []
            for i in range(1, len(rows3)):
                languages.append(rows3[i][0])'''

            languages = StudentDB.getLanguages()

            useLanguages = {}
            for i in range(len(languages)):
                if rows2[0][i+1] == 1:
                    useLanguages[languages[i]] = True
                elif rows2[0][i+1] == 0:
                    useLanguages[languages[i]] = False
                elif rows2[0][i+1] != None:
                    useLanguages[languages[i]] = rows2[0][i+1].split(';')
            student.setUseLanguage(useLanguages)

            student.printStudent()
            print("로그인 성공! 어서오세요 " + s.getName() + "님!")


    conn.close()



s = Student()

print("아이디: ", end="")
s.setID(input())
print("비밀번호: ", end="")
s.setPassword(input())

studentLogin(s)