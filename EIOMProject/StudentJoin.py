import pymysql
from Student import Student




def studentJoin(s):

    conn = pymysql.connect(host='127.0.0.1', user='root', password='hi0310', db='eiom', charset='utf8')
    curs = conn.cursor()

    sql = "INSERT INTO student (`ID`, `password`, `name`, `birth`) values('"+s.getID()+"','"+s.getPassword()+"','"+s.getName()+"','"+s.getBirth().year+"-"+s.getBirth().month+"-"+s.getBirth().day+"');"

    #sql = "INSERT INTO student (`ID`, `password`, `name`, `birth`) values('%s','%s','%s','%s-%s-%s');"
    #data = [[s.getID(), 1], [s.getPassword(), 1], [s.getName(), 1], [s.getBirth().year, 1], [s.getBirth().month, 1], [s.getBirth().day, 1]]
    #conn.cursor().executemany(sql, data)
    #print(sql)

    curs.execute(sql)
    conn.commit()

    conn.close()

#####
s = Student()

print("이름: ", end="")
s.setName(input())
print("아이디: ", end="")
s.setID(input())
print("비밀번호: ", end="")
s.setPassword(input())
print("생년월일")
print("년도: ", end="")
birth_year = input()
print("월: ", end="")
birth_month = input()
print("일: ", end="")
birth_day = input()

s.setBirth(birth_year, birth_month, birth_day)
studentJoin(s)