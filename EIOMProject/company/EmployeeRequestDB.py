from BasicInfo import BasicDB
from company.Company import Company
import operator


def insertRequest(cid, recruit, hopeperson, apply, royalty, document, uselang, employemnt, work, money, worktime,
                  benefit, period, pmoney, manager_email, manager_ph):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    c = Company()
    c.request_authority = 1

    sql = "insert into employment_request (company_id,recruit, hopeperson, apply, royalty, " \
          "document,uselang, employment,work,money,worktime," \
          "benefit,period,pmoney,manager_email,manager_ph) values ('" + cid + "','" + \
          recruit + "','" + hopeperson + "','" + apply + "','" + royalty + "','" + document + "','" + uselang + "','" + employemnt + "','" + work + "','" + money \
          + "','" + worktime + "','" + benefit + "','" + period + "','" + pmoney + "','" + manager_email + "','" + manager_ph + "','" + hopeperson + "');"

    curs.execute(sql)

    BestLang(uselang)


def saveRequest():
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()


def BestLang(str):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    str = str.replace(' ', '')
    list = str.split(',')

    for i in range(0, len(list)):
        list[i] = list[i].upper()

    sql = "select  * from best_lang"

    curs.execute(sql)

    row = curs.fetchall()

    java = row[0][0]
    c = row[0][1]
    cpp = row[0][2]
    cs = row[0][3]
    javascript = row[0][4]
    jquery = row[0][5]
    nodejs = row[0][6]
    react = row[0][7]
    python = row[0][8]
    php = row[0][9]
    jsp = row[0][10]
    mysql = row[0][11]
    servlet = row[0][12]
    android = row[0][13]
    linux = row[0][14]
    oracle = row[0][15]
    spring = row[0][16]
    kotlin = row[0][17]

    for i in range(0, len(list)):
        if list[i] == 'JAVA' or list[i] == '자바':
            java += 1
        elif list[i] == 'C':
            c += 1
        elif list[i] == 'C++':
            cpp += 1
        elif list[i] == 'C#':
            cs += 1
        elif list[i] == 'JAVASCRIPT' or list[i] == 'JS':
            javascript += 1
        elif list[i] == 'JQUERY':
            jquery += 1
        elif list[i] == 'NODEJS' or list[i] == 'NODE.JS':
            nodejs += 1
        elif list[i] == 'REACT' or list[i] == '리액트':
            react += 1
        elif list[i] == 'PYTHON' or list[i] == '파이썬':
            python += 1
        elif list[i] == 'php':
            php += 1
        elif list[i] == 'jsp':
            jsp += 1
        elif list[i] == 'MYSQL':
            mysql += 1
        elif list[i] == 'SERVLET' or list[i] == '서블릿':
            servlet += 1
        elif list[i] == 'ANDROID' or list[i] == '안드로이드':
            android += 1
        elif list[i] == 'LINUX' or list[i] == '리눅스':
            linux += 1
        elif list[i] == 'ORACLE' or list[i] == '오라클':
            oracle += 1
        elif list[i] == 'SPRING' or list[i] == '스프링':
            spring += 1
        elif list[i] == 'KOTLIN' or list[i] == '코틀린':
            kotlin += 1

    sql = 'update best_lang set java=' + java + ', c=' + c + ', cpp=' + cpp + ',cs=' + cs + ', javascript=' + javascript + ', jquery=' + jquery + \
          ', nodejs=' + nodejs + ', react=' + react + ', python=' + python + ', php=' + php + ', jsp=' + jsp + ', msql=' + mysql + ', servlet=' + servlet + \
          ', android=' + android + ', linux=' + linux + ', oracle= ' + oracle + ', spring=' + spring + ', kotlin=' + kotlin;
    curs.execute(sql)
    conn.commit()


def orderByBestLang():
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "select  * from best_lang"

    curs.execute(sql)

    row = curs.fetchall()
    lang = {}
    lang['java'] = row[0][0]
    lang['c'] = row[0][1]
    lang['cpp'] = row[0][2]
    lang['cs'] = row[0][3]
    lang['javascript'] = row[0][4]
    lang['jquery'] = row[0][5]
    lang['nodejs'] = row[0][6]
    lang['react'] = row[0][7]
    lang['python'] = row[0][8]
    lang['php'] = row[0][9]
    lang['jsp'] = row[0][10]
    lang['mysql'] = row[0][11]
    lang['servlet'] = row[0][12]
    lang['android'] = row[0][13]
    lang['linux'] = row[0][14]
    lang['oracle'] = row[0][15]
    lang['spring'] = row[0][16]
    lang['kotlin'] = row[0][17]

    sorted(lang.items(), key=lambda x: x[1], reverse=True)
    return lang
