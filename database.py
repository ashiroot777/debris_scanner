import mysql.connector as m
mydb=m.connect(host='localhost',user='root',password='ashi123')
c=mydb.cursor()

c.execute('show databases;')
databases = c.fetchall()
if ('debris',) in databases:
    overwrite = input('there seems to be another database with the same name, do you want to replace it? type yes or no')
    if overwrite == 'yes':
        c.execute('drop database debris;')
    else:
        print('try again!')

<<<<<<< HEAD
<<<<<<< HEAD
c.execute("create database AAA;")
c.execute("use")
=======
#ashi
>>>>>>> d7d39c680bb770d6ef160419737db6fee3587111
=======
>>>>>>> af43f6d770837cb8f18434379c308fe04c951003
