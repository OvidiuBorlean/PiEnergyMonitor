import smtplib

import config
#subject = ''
#message = ''
def send_email(subject, message):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL_ADDRESS, config.PASSWORD)
		message = 'Subject: {}	{}'.format(subject, message)
		server.sendmail(config.EMAIL_ADDRESS, 'destination_email@gmail.com', message)
		server.quit()
		print ('Email sent succes')
	except:
		print ('Error')


