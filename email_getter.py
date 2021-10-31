import re

f = open('embassies.txt', 'r', encoding='utf-8')
passFile = open('list_emails.txt', 'w')

for line in f:
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line)
    for email in emails:
        passFile.write(email)
        passFile.write("\n")


f.close()
passFile.close()
