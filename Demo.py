import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="S@lakki14",database="Demo")
mycursor = mydb.cursor()
mycursor.execute("Select * from city;")
for i in mycursor:
    print ((i))

mydb.commit()

