import pymysql
from Student import Student





def studentLogin(student):
    conn = pymysql.connect(host='127.0.0.1', user='root', password='hi0310', db='eiom', charset='utf8')
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

            sql = "DESCRIBE languages;"
            curs.execute(sql)
            rows3 = curs.fetchall()

            Languages = []
            for i in range(1, len(rows3)):
                Languages.append(rows3[i][0])

            useLanguages = {}
            for i in range(len(Languages)):
                if rows2[0][i+1] == 1:
                    useLanguages[Languages[i]] = True
                elif rows2[0][i+1] == 0:
                    useLanguages[Languages[i]] = False
                elif rows2[0][i+1] != None:
                    useLanguages[Languages[i]] = rows2[0][i+1].split(';')
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