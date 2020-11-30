
import pymysql

from BasicInfo import BasicDB
from student.Student import Student, Languages
from student import StudentDB


def studentJoin(student, languages=Languages()):
    try:
        student.print()

        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()

        if not (len(student.getPortfolio()) > 0 and len(student.getIntroduce()) > 0):
            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `email`) VALUES ('" + student.getID() + "', '" + student.getPassword() + "', '" + student.getName() + "', '" + student.getMajor() + "', " + str(
                student.getGrade()) + ", " + str(student.getClass()) + ", '" + student.getEmail() + "');"
        elif len(student.getPortfolio()) > 0:
            # 포폴 추가
            pass
        elif len(student.getIntroduce()) > 0:
            # 자소서 추가
            pass
        else:
            # 포폴, 자소서 추가
            pass

        curs.execute(sql)
        conn.commit()

        sql = "INSERT INTO `eiom_db`.`languages` (`id`, `java`, `c`, `cpp`, `cs`, `html`, `css`, `javascript`, `jquery`, `nodejs`, `react`, `python`, `php`, `jsp`, `msql`, `servlet`, `adroid`, `linux`, `oracle`, `spring`, `kotlin`, `etc`) VALUES ('" + student.getID() + "', " + getBool(
            languages.java) + ", " + getBool(languages.c) + ", " + getBool(languages.cpp) + ", " + getBool(
            languages.cs) + ", " + getBool(languages.html) + ", " + getBool(languages.css) + ", " + getBool(
            languages.js) + ", " + getBool(languages.jq) + ", " + getBool(languages.node) + ", " + getBool(
            languages.react) + ", " + getBool(languages.py) + ", " + getBool(languages.php) + ", " + getBool(
            languages.jsp) + ", " + getBool(languages.mysql) + ", " + getBool(languages.servlet) + ", " + getBool(
            languages.android) + ", " + getBool(languages.linux) + ", " + getBool(languages.oracle) + ", " + getBool(
            languages.spring) + ", " + getBool(languages.kotlin) + ", '" + languages.etc + "');"

        curs.execute(sql)
        conn.commit()

        conn.close()
        return True
    except Exception  as ex:
        print(ex)
        return False




def getBool(a):
    if(a):
        return '1'
    else:
        return '0'
#####
'''
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


studentJoin(Student)'''