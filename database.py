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


