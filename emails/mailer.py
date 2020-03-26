import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Marcin'
email['to'] = 'marcin.pasiewicz@gmail.com'
email['subject'] = 'You won new life'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')
print(email)

# with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
#     smtp.ehlo()
#     smtp.starttls()
    # smtp.login('zerotomastery1@gmail.com', 'helloztmoldfriend1')
    # smtp.send_message(email)
