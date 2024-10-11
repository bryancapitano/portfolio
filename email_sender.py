import smtplib
from email.message import EmailMessage

me = 'bryancapitano@gmail.com'
to_email = 'bryan@syncinteractive.com'

def send_email(from_email, subject, message):
    email = EmailMessage()
    email['Subject'] = 'New Message from Portfolio Website!'
    email['From'] = me
    email['To'] = to_email

    email.set_content(
f'''
FROM: {from_email} 
SUBJECT: {subject}
MESSAGE:
{message}        
''')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls() # connect securely to server
        smtp.login(me, 'dkao okmp zbcg gjto')
        smtp.send_message(email)
        print('all good boss!')

    return

