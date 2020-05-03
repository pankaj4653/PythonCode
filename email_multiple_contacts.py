import os
import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = os.environ.get('GMAIL_USER')
EMAIL_PASS = os.environ.get('GMAIL_PASS')

contacts = ['pankaj.k3353@gmail.com','pankaj.k4653@gmail.com']


msg = EmailMessage()
msg['Subject'] = 'This is MotoGp'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts #', '.join(contacts)
msg.set_content=('MotoGp Image Attached')


files = ['resume.pdf']

for file in files:
	with open(file,'rb') as f:
		file_data = f.read()
		#file_type = imghdr.what(f.name)
		#print(file_type)
		file_name = f.name


	msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)



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
	
