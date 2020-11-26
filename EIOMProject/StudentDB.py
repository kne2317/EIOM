import pymysql
from Student import Student


def getLanguages():
    conn = pymysql.connect(host='localhost', user='eiom', password='1111', db='eiom_db', charset='utf8')
    curs = conn.cursor()

    sql = "DESCRIBE languages;"
    curs.execute(sql)
    rows1 = curs.fetchall()

    languages = []
    for i in range(1, len(rows1)):
        languages.append(rows1[i][0])

    return languages

