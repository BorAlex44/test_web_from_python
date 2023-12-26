import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from_addr = 'alexander44@bk.ru'
to_addr = 'alexander44@bk.ru'
my_pass = 'YgqURxp96rH5ckfy5rBz'
report_name = 'log.txt'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Hello, from Alexandr'

with open(report_name, 'rb') as file:
    part = MIMEApplication(file.read(), Name=basename(report_name))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(report_name)
    msg.attach(part)

body = 'This is test message'
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(from_addr, my_pass)
text = msg.as_string()
server.sendmail(from_addr, to_addr, text)
server.quit()

