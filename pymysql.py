import pymysql

try
    db = pymysql.connect("localohost","root","suman","flash_app")
    cursor1=db.cursor()
sql="""CREATE TABLE food_name(id INT,food_name Varchar(30),country Varchar(300))"""
    cursor1.execute(sql)
    print("SUCCESS TABLE CREATD!")
    db.close()

except
 print("Error:Cannot create table!")