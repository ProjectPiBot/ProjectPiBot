import pymysql

def schedule_insert(date, content):
    con = pymysql.connect(host='localhost', user='root', password='1234', db='pdb', charset='utf8') 
    cur = con.cursor()                                                                          
    sql = "insert into schedule values ('" + date + "','" + content + "')"
    cur.execute(sql)
    con.commit()
    con.close()

def schedule_select(date):
    con = pymysql.connect(host='localhost', user='root', password='1234',
                        db='pdb', charset='utf8')
    cur = con.cursor()
    sql = "select * from schedule where date='" + date +"'"
    cur.execute(sql)
    
    # 데이타 Fetch
    rows = cur.fetchall()
    print(rows)
    con.close()
    return str(rows)

def schedule_update(date, content):
    con = pymysql.connect(host='localhost', user='root', password='1234', db='pdb', charset='utf8') 
    cur = con.cursor()                                                                          
    sql = f'update schedule set content={content} where date={date}'
    cur.execute(sql)
    con.commit()
    con.close()

def schedule_delete(date):
    con = pymysql.connect(host='localhost', user='root', password='1234', db='pdb', charset='utf8') 
    cur = con.cursor()                                                                          
    sql = "delete from schedule where date=" + date
    cur.execute(sql)
    con.commit()
    con.close()
