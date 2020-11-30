from BasicInfo import BasicDB
from company.Company import Company

def insertRequest(recruit, hopeperson, apply, royalty, document, uselang,employemnt,wort,money,worktime,benefit,period,pmoney,manager_email,manager_ph):
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    c = Company()
    c.request_authority=1

    sql="insert into employment_request (recruit, hopeperson, apply, royalty, " \
        "document,uselang, employment,work,money,worktime," \
        "benefit,period,pmoney,manager_email,manager_ph) values ();"