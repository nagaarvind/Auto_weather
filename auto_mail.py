import smtplib
import getpass

def auto_mate():
    userMail = "officialteche@gmail.com"
    password = "yqgd crfb qqdi brto"
    print("password entered:", '*****')
    # senderMail = input('sender_mail:')
    senderMail = "nagaarvind7@gmail.com"
    server = smtplib.SMTP('smtp.gmail.com',587)
    #to start a safe tls., connecting server to send mail to the client
    server.starttls()
    server.login(userMail,password)
    server.sendmail(userMail,senderMail,'take umbrella')
    server.sendmail
    print('mail sent')
    server.quit()


# yqgd crfb qqdi brto

    
