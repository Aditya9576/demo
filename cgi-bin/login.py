#!D:\Python\python.exe
print("Content-Type:text/html\r\n\r\n")

# --------------modules-------------
import cgi
import mysql.connector as msc

cg = cgi.FieldStorage()
email = cg.getvalue('email')
password = cg.getvalue('password')

try:
    mydb = msc.connect(host="localhost",user="root",password="aditya370",port="3305")
    mycursor = mydb.cursor()
    mycursor.execute('use website')
except:
    print('<script>alert("database connectivity error!");</script>')

try:
    mycursor.execute("SELECT * FROM USER WHERE email='{}'".format(email))
    listLength = mycursor.fetchall()
    if (len(listLength)!=0 and (password == listLength[0][5])):
        try:
            fp = open('C:/Apache24/cgi-bin/userEmail.txt','w')
            fp.write('{}'.format(email))
            fp.close()
            fp = open('C:/Apache24/cgi-bin/userPassword.txt','w')
            fp.write('{}'.format(password))
            fp.close()
            print("<script>window.open('http://localhost','_self');</script>")
        except:
            print('<script>alert("userFile Error!");</script>')
    else:
        print("<script>alert('user/password not found!')</script>")
        print("<script>window.open('http://localhost/login.html','_self');</script>")
except:
    print('<script>alert("database connectivity error!");</script>')