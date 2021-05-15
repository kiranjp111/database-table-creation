import mysql.connector as m
mydb=m.connect(host="localhost",user="kiranjp",passwd="root",database="employees")
mycursor= mydb.cursor()
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
