import re
import smtplib
gmail_user = ''
gmail_password = ''

f = open('embassies.txt', 'r', encoding='utf-8')
list_c = []

for line in f:
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line)
    for email in emails:
        list_c.append(email)

sent_from = gmail_user
to = list_c
subject = 'Your country'
body = """
Dear representatives of your country,
I hope you receive this email in good health!
I have recently been captivated by your country and although I would love to visit, as a student my current situation will not allow it. 
I was wondering if you could be so generous as to provide me with some little piece of your country! 
Here is my address:

I would be grateful to receive even the smallest of the tokens.

Thank you so much! 
"""

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')

f.close()
