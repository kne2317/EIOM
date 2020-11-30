from BasicInfo import BasicDB
from student.Student import Student, Languages
import shutil
import os


def StudentJoin(student, languages=Languages()):
    try:
        student.print()

        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()



        if len(student.getPortfolio()) > 0 and len(student.getIntroduce()) > 0:
            # 포폴, 자소서 추가

            pfile_name = student.getPortfolio().split('/')[-1]
            poriginal_path = student.getPortfolio().replace('/'+pfile_name, '')
            pdestination_path = os.path.dirname(os.path.realpath(__file__))+"\\..\\portfolio"
            student.setPortfolio(str(student.getGrade())+"학년"+str(student.getClass())+"반"+student.getName()+"_포트폴리오." + student.getPortfolio().split('.')[-1])
            shutil.copyfile(os.path.join(poriginal_path, pfile_name), os.path.join(pdestination_path, student.getPortfolio()))

            ifile_name = student.getIntroduce().split('/')[-1]
            ioriginal_path = student.getIntroduce().replace('/'+ifile_name, '')
            idestination_path = os.path.dirname(os.path.realpath(__file__))+"\\..\\introduce"
            student.setIntroduce(str(student.getGrade())+"학년"+str(student.getClass())+"반"+student.getName()+"_자기소개서." + student.getPortfolio().split('.')[-1])
            shutil.copyfile(os.path.join(ioriginal_path, ifile_name), os.path.join(idestination_path, student.getIntroduce()))

            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `portfolio`, `introduce`, `email`) VALUES ('" + student.getID() + "', '" + student.getPassword() + "', '" + student.getName() + "', '" + student.getMajor() + "', " + str(
                student.getGrade()) + ", " + str(
                student.getClass()) + ", '" + student.getPortfolio() + "', '" + student.getIntroduce() + "', '" + student.getEmail() + "');"

        elif len(student.getPortfolio()) > 0:
            # 포폴 추가
            pfile_name = student.getPortfolio().split('/')[-1]
            poriginal_path = student.getPortfolio().replace('/'+pfile_name, '')
            pdestination_path = os.path.dirname(os.path.realpath(__file__))+"\\..\\portfolio"
            student.setPortfolio(str(student.getGrade())+"학년"+str(student.getClass())+"반"+student.getName()+"_포트폴리오." + student.getPortfolio().split('.')[-1])
            shutil.copyfile(os.path.join(poriginal_path, pfile_name), os.path.join(pdestination_path, student.getPortfolio()))

            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `portfolio`, `email`) VALUES ('" + student.getID() + "', '" + student.getPassword() + "', '" + student.getName() + "', '" + student.getMajor() + "', " + str(
                student.getGrade()) + ", " + str(student.getClass()) + ", '" + student.getPortfolio() + "', '" + student.getEmail() + "');"

        elif len(student.getIntroduce()) > 0:
            # 자소서 추가
            ifile_name = student.getIntroduce().split('/')[-1]
            ioriginal_path = student.getIntroduce().replace('/' + ifile_name, '')
            idestination_path = os.path.dirname(os.path.realpath(__file__)) + "\\..\\introduce"
            student.setIntroduce(str(student.getGrade())+"학년"+str(student.getClass())+"반" + student.getName() + "_자기소개서." + student.getPortfolio().split('.')[-1])
            shutil.copyfile(os.path.join(ioriginal_path, ifile_name),
                            os.path.join(idestination_path, student.getIntroduce()))

            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `introduce`, `email`) VALUES ('" + student.getID() + "', '" + student.getPassword() + "', '" + student.getName() + "', '" + student.getMajor() + "', " + str(
                student.getGrade()) + ", " + str(student.getClass()) + ", '" + student.getIntroduce() + "', '" + student.getEmail() + "');"

        else:
            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `email`) VALUES ('" + student.getID() + "', '" + student.getPassword() + "', '" + student.getName() + "', '" + student.getMajor() + "', " + str(
                student.getGrade()) + ", " + str(student.getClass()) + ", '" + student.getEmail() + "');"


        curs.execute(sql)
        conn.commit()

        sql = "INSERT INTO `eiom_db`.`languages` (`id`, `java`, `c`, `cpp`, `cs`, `html`, `css`, `javascript`, `jquery`, `nodejs`, `react`, `python`, `php`, `jsp`, `msql`, `servlet`, `android`, `linux`, `oracle`, `spring`, `kotlin`, `etc`) VALUES ('" + student.getID() + "', " + getBool(
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
    except Exception as e:
        print(e)
        return False


def TeacherJoin(teacher):
    try:
        teacher.print()

        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()

        sql = "INSERT INTO `eiom_db`.`teacher` (`id`, `name`, `password`, `email`) VALUES ('" + teacher.getID() + "', '" + teacher.getName() + "', '" + teacher.getPassword() + "', '" + teacher.getEmail() + "');"

        curs.execute(sql)
        conn.commit()

        conn.close()
        return True
    except Exception as e:
        print(e)
        return False


def CompanyJoin(company):
    try:
        company.print()

        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()

        sql = "INSERT INTO `eiom_db`.`teacher` (`id`, `name`, `password`, `email`) VALUES ('" + teacher.getID() + "', '" + teacher.getName() + "', '" + teacher.getPassword() + "', '" + teacher.getEmail() + "');"

        curs.execute(sql)
        conn.commit()

        conn.close()
        return True
    except Exception as e:
        print(e)
        return False



def getBool(a):
    if(a):
        return '1'
    else:
        return '0'