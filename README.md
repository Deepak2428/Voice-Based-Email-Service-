# Voice-Based-Email-Service-
Voice based email service




1.2.2 Software used: 
 
❖	VISUAL  STUDIO CODE
❖	PYTHON 3
❖	Internet connectivity


NOTE: TO MAKE THE PROJECT RUN USER MUST ALLOW THE PERMISSION TO SEND MAILS FROM LESS- SECURE PLATFORMS. THIS OPTION IS AVAILABLE IN SETTINGS OF YOUR ACCOUNT


 
1.3 DESCRIPTION OF PROJECT:

•	PYTTSX3:    It is a library which is to convert text to speech offline. It has many methods some of which have been used in the program.
  (1)	Say (string):  It used to speak the string which is inside the parenthesis.
  (2)	getProperty():  used to get the properties of the speaking engine like voice (mail, female) , rate of speech, volume, id.
  (3)	setProperty() :   used to set the properties like setting rate to 150, volume from 0.1 to 1, voice of male or female. Each word has to be passed as an argument separated by a comma and its value.
  (4)	RunAndWait ():  waits until say function is completed.

•	EMAIL:  This library is used to send email from the program.


•	Speech Recognition:  This library is used for speech recognition. The user will say something. It will Record that audio and convert the recorded text into
   a text and then the program will continue accordingly.


•	Inputaudio:  This is a self-made library and it contains all the function of Speech Recognition library which are required for taking audio input from the user. 
  The purpose of this library is to reduce the code length. Wherever voice input is required we have called takeaudio(string) function of this library. 
  Therefore instead of writing same code again and again we just call it so code length got reduced.


     takeaudio(string):-   it is a function defined in inputaudio library. We call this function whenever there is a need of taking input from the user.
     The input is taken via microphone of the computer. The taken input is then stored in a variable and later google_recognizer() function is used to convert that audio 
     to text. Takeaudio function has a argument string. We will pass one out of these three things as argument in it i.e. normal, message. If:

           	Normal is passed then the duration of recording is reduced to 4 seconds. 

           	Message is passed then the duration of recording is increased to 20 seconds as a message can be long enough.

           	Subject is passed then the time duration will be 7 seconds, as in some cases subject has to describe briefly.


•	Imaplib:  It is a library which is used to receive email from the program. We have to provide username and password in the variables and these library methods
  will log into the account and receive email. 

         	Mail.login(username, password):  login with the username and password provided earlier of the email whose message we want to receive.

         	Mail.Select(“inbox”):  Selects the inbox section out of sent , all mails, outbox.

         	Mail.search() : searches the  all the mail in the email id and returns a space separated byte list which has email id in the form of numbers not as string,
         and a status to clear that mail has been received.

            We have a List by the name mail_ids []. We iterate over the byte list and then store individual number in the list.

            Eg:   search() returns list in the form of : data= [b’1 2 3 4 5 6 7 8’] 
            Then when we iterate over this list it will split from spaces.
            Then mail_ids [] become [b’1, b’2, b’3, b’4, b’5, b’6, b’7, b’8]
 
            Where b’8 is our latest email and b’1 is our last mail.
            We then calculate the Length of the List and extract the last element in this case b’8 and store it in a variable recent_mail b and pass it to fetch() method.

         	Mail.fetch(recent_mail,(RFC882)) : This function fetches the message and its details like senders email, subject , content .
         This function extracts the message from the byte which was present in the list mail_ids.  After that it assigns senders email to mail_from variable, 
         subject to mail_subject variable and message to mail_content variable. 

          After this the program reads the variables.


          *** If the user wants to read all the mails in his/her inbox then the fetch function will be inside a loop which will be iterate all the email ids of the
          list mail_ids[]  and we have to pass the loop controlling variable in mail.fetch() function. 

           Eg:      for i in mail_ids:
                      Status,data =mail.fetch(i,RFC882)
 
          But as the List has elements [b’1, b’2, b’3----, b’8], therefore the last mail of our inbox is read first and then second last and so on. 
          To resolve this issue we can reverse the list before iterating over it. The new list then becomes [b’8, b’7, ------, b’1]. Now our top most mail is read first.


•	Smtplib:  This library is used to send email. Various functions of this library perform different steps to send an email to the desired person.
         
         
         First we set the host as “smtp.gmail.com”. Then we assign our username to from_adrr variable, and senders email address to to_adrrs variable. 
         Similarly we assign message subject to the variables.
 

        	SMPT_SSL (host, port):   used to connect to the host services.

        	Server. Login(username, password): login to the server with the username and password provided in arguments.

        	Server.sendmail(from_adrr, to_addrs, message.as_string()):  used to send email from the address in  from_adrr to the address in  to_addrs. 
        The message is stored is message. It is first converted to string and then sent.

        	Server.quit(): Used to exit the server after sending mail. 


Working:

	To send an email the user will be asked to speak send. The voice will be recorded and converted to text with the help of audio(“string”) function defined in input audio
library 

   	 If string = normal   :  Audio is recorded for 4 seconds
   	If string = subject   :  Audio is recorded for 7 seconds
   	If string = message :  Audio is recorded for 20 seconds

   If he does so then he will be asked to speak the username of the person to whom he wish to send the email.

   A dictionary named contacts has been used which contains username as key and their email addresses as value.

   As user speaks the username. The function audio(“string”) in inputaudio library will convert audio to text and will assign it to receiver variable the program will 
   search the username in the dictionary and will give the corresponding email address.

   Then the email will be assigned to mail_to variable of smtplib library.

   The user then will be asked to speak the subject. 

   The function audio(“string”) will convert audio to text and will assign it to Subject variable of smtplib library. 

   In the end the user will be asked to speak message. 

   The function audio (“string”) will convert audio to text and will assign it to msg variable of smtplib library

   After this the server.send() define in smtplib will send the mail to the desired person. At last the server.quit() function leaves the server and the mail would
   have been sent to the person and the program terminates.

   NOTE:  server will depend from account to account. If your email address is of Gmail the server variable will be:
                      Server= smtplib.gmail.com
   If your account is in outlook the server will be:
                      Server= smtp-mail.outlook.com


 
	To read the latest email from inbox the user will be asked to speak check. 
  inputaudio library audio(“string”) function will take input .
  The program logins to the server by server.login(username, password) then it selects inbox by server.select(“mail”).
  It then stores list of all mail in a list data by using server.search() method. Then we iterate over the list and separate all the mail ids in a list mail_ids []. 
  The last element of our list is our recent mail. We extract that and pass it to the fetch() function which extract all the details like senders mail, 
  subject of mail and message and assign them to variable. After this the program speaks the details and it terminates.  

   After taking input we used imaplib to read the latest email. The program first reads the senders email address then the subject of the mail and at last the message
   of the mail. After this the program terminates.

	If user speaks exit then the program terminates without doing anything.

	If user says something else the program gives appropriate message and then terminates.





YOU MUS HAVE AN INTERNET CONNECTION FOR THIS...
HOPE YOU UNDERSTOOD. THANKS . DO FOLLOW AND SHARE MY PROFILE.
