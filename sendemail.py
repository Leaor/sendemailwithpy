import smtplib
from email.mine.text import MIMEText
from email.mine.text import MIMEMultipart

email = 'example@gmail.com'
password = 'your password'
send_to_email = 'person you send the email to@gmail.com'
subject = 'SUBJECT'
message = 'YOUR MESSAGE'

msg = MIMEMultipart()
msg ['From'] = email
msg ['To'] = send_to_email
msg ['Subject'] = subject
msg.attach(MIMETEXT (message, 'plain'))

server = smtplib.SMTP('smtp@gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
