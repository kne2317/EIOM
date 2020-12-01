from BasicInfo import BasicDB
class Student:
    ID = ''
    password = ''
    name = ''
    email = ''
    major = ''
    grade = -1
    class_ = -1
    portfolio = ''
    introduce = ''
    likeCompany = ''
    def print(self):
        print("id: " + self.ID)
        print("password: " + self.password)
        print("name: " + self.name)
        print("email: " + self.email)
        print("major: " + self.major)
        print("grade: " + str(self.grade))
        print("class_: " + str(self.class_))
        print("portfolio: " + self.portfolio)
        print("introduce: " + self.introduce)
        print("likeCompany: " + self.likeCompany)

class Languages:
    c = False
    cpp = False
    cs = False
    py = False
    html = False
    css = False
    js = False
    jq = False
    jsp = False
    php = False
    node = False
    react = False
    java = False
    spring = False
    servlet = False
    kotlin = False
    android = False
    linux = False
    oracle = False
    mysql = False
    etc = ''

def uselang():
    basicDB = BasicDB()
    conn = basicDB.conn
    curs = conn.cursor()

    sql = "select * from languages where id='"+Student.ID+"';"

    curs.execute(sql)
    row=curs.fetchall()

    lang={}
    if len(row)>0:
        lang['java'] = row[0][0]
        lang['c'] = row[0][1]
        lang['c++'] = row[0][2]
        lang['c#'] = row[0][3]
        lang['html'] = row[0][4]
        lang['css'] = row[0][5]
        lang['javascript']= row[0][6]
        lang['jquery '] = row[0][7]
        lang['node.js'] = row[0][8]
        lang['react'] = row[0][9]
        lang['python'] = row[0][10]
        lang['php'] = row[0][11]
        lang['jsp'] = row[0][12]
        lang['mysql'] = row[0][13]
        lang['servlet'] = row[0][14]
        lang['android'] = row[0][15]
        lang['linux'] = row[0][16]
        lang['oracle'] = row[0][17]
        lang['spring'] = row[0][18]
        lang['kotlin'] = row[0][19]

    for key,values in lang.items():
        if values==False:
            del lang[key]

    use=list(lang.keys())
    u=', '.join(use)
    return u