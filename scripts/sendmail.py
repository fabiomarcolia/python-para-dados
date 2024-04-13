

import smtplib

my_email = "seuemail@dominio.com"
password = "suasenha"

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email, password=password)

connection.sendmail(from_addr=my_email,to_addrs="destinatario@dominio.com", msg="Hello World")

connection.close()
