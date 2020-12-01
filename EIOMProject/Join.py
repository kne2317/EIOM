from BasicInfo import BasicDB
from company.Company import Company
from student.Student import Student, Languages
from teacher.Teacher import Teacher
import shutil
import os



def StudentJoin( languages=Languages()):
    try:
        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()



        if len(Student.portfolio) > 0 and len(Student.introduce) > 0:
            # 포폴, 자소서 추가

            pfile_name = Student.portfolio.split('/')[-1]
            poriginal_path = Student.portfolio.replace('/'+pfile_name, '')
            pdestination_path = os.path.dirname(os.path.realpath(__file__))+"\\\portfolio"
            Student.portfolio = str(Student.grade)+"학년"+str(Student.class_)+"반"+Student.name+"_포트폴리오." + Student.portfolio.split('.')[-1]
            shutil.copyfile(os.path.join(poriginal_path, pfile_name), os.path.join(pdestination_path, Student.portfolio))

            ifile_name = Student.introduce.split('/')[-1]
            ioriginal_path = Student.introduce.replace('/'+ifile_name, '')
            idestination_path = os.path.dirname(os.path.realpath(__file__))+"\\introduce"
            Student.introduce = str(Student.grade)+"학년"+str(Student.class_)+"반"+Student.name+"_자기소개서." + Student.portfolio.split('.')[-1]
            shutil.copyfile(os.path.join(ioriginal_path, ifile_name), os.path.join(idestination_path, Student.introduce))

            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `portfolio`, `introduce`, `email`) VALUES ('" + Student.ID + "', '" + Student.password + "', '" + Student.name + "', '" + Student.major + "', " + str(
                Student.grade) + ", " + str(Student.class_) + ", '" + Student.portfolio + "', '" + Student.introduce + "', '" + Student.email + "');"

        elif len(Student.portfolio) > 0:
            # 포폴 추가
            pfile_name = Student.portfolio.split('/')[-1]
            poriginal_path = Student.portfolio.replace('/' + pfile_name, '')
            pdestination_path = os.path.dirname(os.path.realpath(__file__)) + "\\portfolio"
            Student.portfolio = str(Student.grade) + "학년" + str(Student.class_) + "반" + Student.name + "_포트폴리오." + \
                                Student.portfolio.split('.')[-1]
            shutil.copyfile(os.path.join(poriginal_path, pfile_name), os.path.join(pdestination_path, Student.portfolio))

            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `portfolio`, `email`) VALUES ('" + Student.ID + "', '" + Student.password + "', '" + Student.name + "', '" + Student.major + "', " + str(
                Student.grade) + ", " + str(Student.class_) + ", '" + Student.portfolio + "', '" + Student.email + "');"

        elif len(Student.introduce) > 0:
            # 자소서 추가
            ifile_name = Student.introduce.split('/')[-1]
            ioriginal_path = Student.introduce.replace('/' + ifile_name, '')
            idestination_path = os.path.dirname(os.path.realpath(__file__)) + "\\introduce"
            Student.introduce = str(Student.grade) + "학년" + str(Student.class_) + "반" + Student.name + "_자기소개서." + \
                                Student.portfolio.split('.')[-1]
            shutil.copyfile(os.path.join(ioriginal_path, ifile_name),
                            os.path.join(idestination_path, Student.introduce))

            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `introduce`, `email`) VALUES ('" + Student.ID + "', '" + Student.password + "', '" + Student.name + "', '" + Student.major + "', " + str(
                Student.grade) + ", " + str(Student.class_) + ", '" + Student.introduce + "', '" + Student.email + "');"

        else:
            sql = "INSERT INTO `eiom_db`.`student` (`id`, `password`, `name`, `major`, `grade`, `class`, `email`) VALUES ('" + Student.ID + "', '" + Student.password + "', '" + Student.name + "', '" + Student.major + "', " + str(
                Student.grade) + ", " + str(Student.class_) + ", '" + Student.email + "');"


        curs.execute(sql)
        conn.commit()

        sql = "INSERT INTO `eiom_db`.`languages` (`id`, `java`, `c`, `cpp`, `cs`, `html`, `css`, `javascript`, `jquery`, `nodejs`, `react`, `python`, `php`, `jsp`, `msql`, `servlet`, `android`, `linux`, `oracle`, `spring`, `kotlin`, `etc`) VALUES ('" + Student.ID + "', " + getBool(
            Languages.java) + ", " + getBool(Languages.c) + ", " + getBool(Languages.cpp) + ", " + getBool(
            Languages.cs) + ", " + getBool(Languages.html) + ", " + getBool(Languages.css) + ", " + getBool(
            Languages.js) + ", " + getBool(Languages.jq) + ", " + getBool(Languages.node) + ", " + getBool(
            Languages.react) + ", " + getBool(Languages.py) + ", " + getBool(Languages.php) + ", " + getBool(
            Languages.jsp) + ", " + getBool(Languages.mysql) + ", " + getBool(Languages.servlet) + ", " + getBool(
            Languages.android) + ", " + getBool(Languages.linux) + ", " + getBool(Languages.oracle) + ", " + getBool(
            Languages.spring) + ", " + getBool(Languages.kotlin) + ", '" + Languages.etc + "');"

        curs.execute(sql)
        conn.commit()

        conn.close()
        return True
    except Exception as e:
        print(e)
        return False


def TeacherJoin():
    try:

        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()

        sql = "INSERT INTO `eiom_db`.`teacher` (`id`, `name`, `password`, `email`) VALUES ('" + Teacher.ID + "', '" + Teacher.name + "', '" + Teacher.password + "', '" + Teacher.email + "');"

        curs.execute(sql)
        conn.commit()

        conn.close()
        return True
    except Exception as e:
        print(e)
        return False


def CompanyJoin():
    try:
        basicDB = BasicDB()
        conn = basicDB.conn
        curs = conn.cursor()

        sql = "INSERT INTO `eiom_db`.`company` (`companyname`, `id`, `password`, `address`, `annualsales`," \
              " `web`, `email`, `manager_name`, `manager_ph`,request_authority, pfauthority) " \
              "VALUES ('"+Company.companyname+"', '"+Company.ID+"', '"+Company.password +"', '"+Company.address+"', '"+\
              Company.annualsale+"', '"+Company.web+"', '"+Company.email+"', '"+Company.manager_name+"', '"+Company.manager_ph+"',"+0+","+0+");"

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