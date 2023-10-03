import pymysql

try
    db = pymysql.connect("localohost","root","suman","flash_app")
    cursor1=db.cursor()
sql="""CREATE TABLE food_name(id INT,food_name -origin values("pizza","italy")))"""
    cursor1.execute(sql)
    print("Data inserted successfully!")
    db.close()

except
 print("Error in your database connection")