import smtplib
from email.message import EmailMessage

def email_alert(sub, body, to):
  msg = EmailMessage()
  msg.set_content(body)
  msg['subject'] = sub
  msg['to'] = to

  user = "anonym2529@gmail.com"  
  password = "wpvmyysuxxkjsrme"

  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(user, password)
  server.send_message(msg)
  server.quit()

if __name__ == "__main__":
  for i in range(10000):
    email_alert('subject',  'msg', 'gmail')