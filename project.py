#   DEEPAK GODIYAL
#   SECTION A  , ROLL NO 20
#   UNIVERSITY ROLLNO - 2014627


# Must have internet connection to execute the code


import pyttsx3         #library to use text to speech
import email           #LIBRARY FOR SENDING MAIL    
import speech_recognition as sr  # for recording audio
import inputaudio

eng=pyttsx3.init()
eng.setProperty("rate",150)
voices=eng.getProperty('voices')
eng.setProperty("voice", voices[0].id)

#intro begins
#eng.say(" hello deepak wELCOME TO VOICE BASED EMAIL")
#eng.say("speak Send  if you wish to send an email ")
#eng.say("speak  check if you wish Check inbox And read email")
#eng.say("speak exit if you wish to Exit the System")
eng.say(" i am listening ")
eng.runAndWait() 

#taking audio input from user

input=inputaudio.takeaudio("normal")
print(input)

#taking actions according to input


# dictionary which contains username and their email address

contacts={"abc":"abcexample@gmail.com","def":"defexample@yahoo.com","efg":"efgexample@outlook.com"}

# when the program runs you are required to speak the username eg. abc    or   def.

if input =="Send" or input == "send":
    
    # we have to send email

    
    username=""   #write your email here
    password=""   #write your password here
    
    #taking audio input from user to speak the contact which he wants to send mail
   
    eng.say("HELLO DEEPAK .. HOPE YOU ARE FINE . speak USERNAME to whom you want to send mail.")
    eng.runAndWait()
    eng.say("speak now  :")
    eng.runAndWait()
    temp= inputaudio.takeaudio("normal")
    
    print(temp)     #printing username to see if correct audio has been converted to text
    
    receiver=contacts[temp]   #extracting email from the dictionary above
    
    print(receiver)  #printing the email id of the user  
    
    #     recording subject and message of email 

    eng.say("what is the subject :")
    eng.runAndWait()
    subject=inputaudio.takeaudio("subject")

     #     recording message from the user

    eng.say("speak your message")
    eng.runAndWait()
    msg=inputaudio.takeaudio("message")
    print(msg)
     
     # sending mail through smtplib 
    
    
    import smtplib
    from email.mime.text import MIMEText
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    from_addr = username
    to_addrs = receiver

    message = MIMEText(msg)
    message['subject'] = subject
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    eng=pyttsx3.init()
    eng.setProperty("rate",150)
    server.quit()
    eng.say("your message has been sent succesfully.. Thank you for using voice based email..good bye")
    eng.runAndWait()


    # receiving mail


elif input=="check" or input=="Check":
    #reading latest mail in inbox
    
    
    eng.say("ok checking your latest mail and reading ")
    eng.runAndWait()
    import imaplib
    username=""      # enter the email from whose inbox you want to read the mail
    password=""      # enter the password of the mail
    SERVER = 'outlook.office365.com'     #server of the email. if gmail use  imaplib.gmail.com
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(username,password)
    mail.select('inbox')
    status, data = mail.search(None, 'ALL')
    mail_ids = []
    for block in data:
        mail_ids += block.split() 
   

   # the library had a loop to iterate over the entire list of mail id but here i have changed code little bit
   # Not running loop through the entire list . instead calculated the length of list
   #  and passed last element of list as it is our latest mail and passing it as argument to fetch function.
    
    
    length=len(mail_ids)
    recent_mail=mail_ids[length-1]
    
    status, data = mail.fetch(recent_mail, '(RFC822)')
    for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']
                if message.is_multipart():
                    mail_content = ''

                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                            
                else:
                    mail_content = message.get_payload()
                   
                eng.say("ok.. Mail from ")
                eng.say(mail_from)
                eng.say("subject of mail is ")
                eng.say(mail_subject)
                eng.say("mail says ")
                eng.say(mail_content)  
                eng.runAndWait()
   
    eng.say("thanks for using voice based email.. good bye ")
    eng.runAndWait()
    exit()


    #  if we wish to read all the mail then we have to iterate in mail_ids then status , data will be within
    #   that loop.  but it will read from bottom to top as the list is like [b'1 , b'2 , b'3,-----,b'n]
    #   where b'n  is our recent top most  mail and b'1 is the last mail of inbox. 
    #   to make read all the mails but from top to bottom we can reverse the list. by  mail_ids.reverse()
    #   the list then becomes [b'n , b'n-1 , --------, b'2 , b'1].. then we have to pass i as argument 
    #   in fetch() method instead of recent_mail...


elif input=="Exit" or input=="exit":

    eng.say("ok .. exiting .. thanks for using voice mail.. GOOD BYE ")
    eng.runAndWait()
    exit()

else:

    eng.say(" you have entered wrong choice sir.. exiting the program.. good bye ")
    eng.runAndWait()
    exit()
    

    
