from BasicInfo import BasicDB
from company.Company import Company
from company.Company import Request
import Login

def updateCompanyInfo(companyname,employees_num,major,annualsale,introduce,web,address):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql="update company set companyname='"+companyname+"', employees_num="+employees_num+", major='"+major+\
        "', annualsales='"+annualsale+"', introduce='"+introduce+"', web='"+web+"',address='"+address+\
        "' where id='"+Company.ID+"';"
    curs.execute(sql)
    conn.commit()

    Login.saveCompanyInfo();

def insertRequest(cid, recruit, hopeperson, apply, royalty, document, uselang, employemnt, work, money, worktime,
                  benefit, period, pmoney, manager_email, manager_ph):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "insert into employment_request (company_id,recruit, hopeperson, apply, royalty, "+ \
          "document,uselang, employment,work,money,worktime,"+ \
          "benefit,period,pmoney,manager_email,manager_ph) values ('" + cid + "','" + \
          recruit + "','" + hopeperson + "','" + apply + "','" + royalty + "','" + document + "','" + uselang + "','" + employemnt + "','" + work + "','" + money \
          + "','" + worktime + "','" + benefit + "','" + period + "','" + pmoney + "','" + manager_email + "','" + manager_ph + "');"

    curs.execute(sql)
    conn.commit()
    BestLang(uselang)

    Company.request_authority=1

    callRequest()

def callRequest():
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "select *  from employment_request where company_id='"+Company.ID+"';"
    curs.execute(sql)
    row=curs.fetchall()
    if len(row)>0:
        Request.id = row[0][0]
        Request.company_id = row[0][1]
        Request.recruit = row[0][2]
        Request.hopeperson = row[0][3]
        Request.apply = row[0][4]
        Request.royalty = row[0][5]
        Request.document = row[0][6]
        Request.uselang = row[0][7]
        Request.employment = row[0][8]
        Request.work = row[0][9]
        Request.money = row[0][10]
        Request.worktime = row[0][11]
        Request.benefit = row[0][12]
        Request.period = row[0][13]
        Request.pmoney = row[0][14]
        Request.manager_email = row[0][15]
        Request.manager_ph = row[0][16]



def BestLang(k):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    k = k.replace(' ', '')
    list = k.split(',')

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

    sql = 'update best_lang set java=' + str(java) + ', c=' + str(c) + ', cpp=' + str(cpp) + \
          ',cs=' + str(cs) + ', javascript=' + str(javascript) + ', jquery=' + str(jquery) + \
          ', nodejs=' + str(nodejs) + ', react=' + str(react) + ', python=' + str(python) + \
          ', php=' + str(php) + ', jsp=' + str(jsp) + ', msql=' + str(mysql) + ', servlet=' + str(servlet) + \
          ', android=' + str(android) + ', linux=' + str(linux) + ', oracle= ' + str(oracle) +\
          ', spring=' + str(spring) + ', kotlin=' + str(kotlin);
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
