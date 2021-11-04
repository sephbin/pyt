import smtplib

gmail_user = 'cox.sync.boat@gmail.com'
gmail_password = 'Britvahcritson10%'

sent_from = gmail_user
# to = ['emily.leung@cox.com.au']
to = ['andrew.butler@cox.com.au']
subject = 'OMG Super Important Message'
body = 'Joking.'

email_text = """\
From: Sync Boat
To: %s
X-Priority: 1
Subject: %s

%s\r\n


""" % (", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print ('Something went wrong...')