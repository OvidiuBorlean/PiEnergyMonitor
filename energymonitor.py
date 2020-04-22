import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import schedule
from sendmail import send_email
import datetime

mail_sent_on = False
mail_sent_off = False
#global alarm
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def sendmail():
        print("Temorary function")

def runtime():
           global alarm

           if GPIO.input(10) == GPIO.LOW:
              print("Alarm-ON")
              alarm = True
           else:
                alarm = False
                print("Alarm-OFF")
           return bool(alarm)

#schedule.every(5).seconds.do(runtime)
#schedule.every(15).seconds.do(sendmail)

if __name__ == '__main__':


        while True:
                time.sleep(5)
                currenttime = datetime.datetime.now()
		a = runtime()

                #schedule.run_pending()
                #print (a, mail_sent)
                if a == True and  mail_sent_on == False:
                        sendmail()
                        send_email("Alarm ON", "Location")
                        mail_sent_on = True
			with open ("energy.logs",'a') as myfile:
                             myfile.write("Alarm ON " + str(currenttime) + '\n')
			     myfile.close()
			
                #print (mail_sent_on, a, mail_sent_off)
                if mail_sent_on == True and a == False:
                        print ("Alarm OFF")
                        send_email("Alarm OFF ", "Location")
                        mail_sent_on = False
                        with open ("energy.logs",'a') as myfile:
                             myfile.write("Alarm OFF " + str(currenttime) + '\n')
                             myfile.close()




