import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('GMAIL_USER')
EMAIL_PASS = os.environ.get('GMAIL_PASS')


msg = EmailMessage()
msg['Subject'] = 'Grab Dinner this Weekend ?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'pankaj.k4653@gmail.com'
msg.set_content=('How about Dinner at 6pm this Saturday ?')
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	#smtp.ehlo()#idetify yourself to the smtp server and it is called automatically in the background
	#smtp.starttls() #encrypt our traffic
	#smtp.ehlo()#Reidetify yourself as encrypted connection

	smtp.login(EMAIL_ADDRESS,EMAIL_PASS)


# Plain Text Email from Scratch

	#subject = 'Grab Dinner this Weekend ?'
	#body = 'How about Dinner at 6pm this Saturday ?'

	#msg =f"Subject: {subject} \n\n\n {body}"

	#smtp.sendmail(SENDER, RECEIVER, msg)

	smtp.send_message(msg)


	#You can test this by using a local DEBUG SERVER 
	#python3 -m smtpd -c DebuggingServer -n localhost:1025
	#This local server will listen to email to our local machine
	