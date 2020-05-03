import os
import smtplib

EMAIL_ADDRESS = os.environ.get('GMAIL_USER')
EMAIL_PASS = os.environ.get('GMAIL_PASS')

#with smtplib.SMTP('smtp.gmail.com',587) as smtp:
with smtplib.SMTP('localhost',1025) as smtp:
	# smtp.ehlo()#idetify yourself to the smtp server and it is called automatically in the background
	# smtp.starttls() #encrypt our traffic
	# smtp.ehlo()#Reidetify yourself as encrypted connection

	# smtp.login(EMAIL_ADDRESS,EMAIL_PASS)

# Plain Text Email from Scratch

	subject = 'Grab Dinner this Weekend ?'
	body = 'How about Dinner at 6pm this Saturday ?'

	msg =f"Subject: {subject} \n\n\n {body}"

	#smtp.sendmail(SENDER, RECEIVER, msg)

	smtp.sendmail(EMAIL_ADDRESS, 'pankaj.k4653@gmail.com', msg)


	#You can test this by using a local DEBUG SERVER 
	#python3 -m smtpd -c DebuggingServer -n localhost:1025
	#This local server will listen to email to our local machine
	