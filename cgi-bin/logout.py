#!D:\Python\python.exe
print("Content-Type:text/html\r\n\r\n")

#------------ open user and password file-----------------
try:
    fp = open("C:/Apache24/cgi-bin/userEmail.txt","w")
    fp.close()
    fp = open("C:/Apache24/cgi-bin/userPassword.txt","w")
    fp.close()
    print("<script>window.open('http://localhost/cgi-bin/login.py','_self');</script>")
except:
    print('<script>alert("DataBase Error !")</script>')