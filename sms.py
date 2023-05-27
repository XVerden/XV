import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

FromAddr = "Hehe@gmail.com"
ToAddr = input("[+]Send email to: ")
name = input("Full name: ")
link = input("[+]Insert Link: ")
BackAddr = "trendergrobler@gmail.com"

msg = MIMEMultipart()
msg["From"] = input("[+]Spoofed name: ") + f" <{FromAddr}>"
msg["Reply-To"] = BackAddr
msg["To"] = ToAddr
msg["Subject"] = input("[+]Add Email Subject: ")

Body = f"""Dear {name}.
We noticed Suspicious activity in your account. 
Your account deatils at {ToAddr} have been compromised.

Go to our Recovery Page {link} to recover your data.
Contact: 078 421 881
Support: {link}

Thank You."""
msg.attach(MIMEText(Body, "plain"))

SMTPServer = smtplib.SMTP("smtp.gmail.com", 587)
SMTPServer.ehlo()
SMTPServer.starttls()
SMTPServer.login(BackAddr, "lsrggymoxlbevoqg")
SMTPServer.sendmail(FromAddr, ToAddr, msg.as_string())
SMTPServer.quit()