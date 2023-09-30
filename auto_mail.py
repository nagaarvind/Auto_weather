import smtplib
import getpass

userMail = input('user_mail:')
password = getpass.getpass("enter pass: ")
senderMail = input('sender_mail:')
print("password entered:", '*****')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login(userMail,password)

server.sendmail(userMail,senderMail,'mail sent from python code from input from the user')

print('mail sent')

server.quit()
# yqgd crfb qqdi brto