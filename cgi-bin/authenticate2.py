#!D:\Python\python.exe
print("Content-Type:text/html\r\n\r\n")

#------------ open user and password file-----------------
try:
    fp = open("C:/Apache24/cgi-bin/userEmail.txt","r")
    userEmail = fp.read();
    fp.close()
    try:
        fp = open("C:/Apache24/cgi-bin/userPassword.txt","r")
        userPassword = fp.read();
        fp.close()
    except:
        print('<script>alert("PASSWORD  ERROR !")</script>')
except:
    print('<script>alert("Email  ERROR !")</script>')

if len(userEmail)!=0:
    print("<script>window.open('http://localhost/payment.html','_self');</script>")
else:
    print("<script>window.open('http://localhost/login.html','_self');</script>")
