import mysql.connector as m
mydb=m.connect(host="localhost",user="kiranjp",passwd="root",database="employees")
mycursor= mydb.cursor()
mycursor.execute("insert into customer values()",
                 "('kiran','vennala')")


