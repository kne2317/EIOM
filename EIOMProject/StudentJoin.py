import pymysql
from Student import Student
import StudentDB


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
student = Student()

print("이름: ", end="")
student.setName(input())

print("아이디: ", end="")
student.setID(input())

print("비밀번호: ", end="")
student.setPassword(input())

while(True):
    print("생년월일(ex: 2000-01-01): ", end="")
    birth = input()
    if len(birth) == 10:
        if birth[4] == "-" and birth[7] == "-":
            birth = birth.split("-")
            break
    print("잘못된 입력입니다")
student.setBirth(birth[0], birth[1], birth[2])

print("사용 가능 언어(true/false)")
languages = StudentDB.getLanguages()

useLanguages = {}
for i in range(len(languages)-1):
    while(True):
        print(languages[i] + ": ", end="")
        answer = input()
        if answer == "true":
            useLanguages[languages[i]] = True
            break;
        elif answer == "false":
            useLanguages[languages[i]] = False
            break;
        else:
            print("잘못된 입력입니다.")

print("제시된 언어 이외에도 사용 가능한 언어(있으면 ;으로 구분하여 입력(ex: visual vasic;ruby;R), 없으면 false)")
answer = input()
if answer != "false" and answer != None:
    useLanguages[languages[-1]] = answer.split(';')
else:
    useLanguages[languages[-1]] = None

student.setUseLanguage(useLanguages)

print("관심 있는 회사(있으면 ;으로 구분하여 입력(ex: Naver;Google;Kakao), 없으면 false): ")
answer = input()
if answer != "false" and answer != None:
    student.setLikeCompany(answer.split(";"))

print("----------------------")
student.printStudent()


studentJoin(Student)