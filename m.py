import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

sender_email = str(raw_input("Enter your mail address"))
receiver_email = str(raw_input("Enter the receiver email: "))
subject = raw_input("Enter the Subject: ")
body = raw_input("Type content of Body: ")





message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email


message.attach(MIMEText(body, "plain"))
file_send=raw_input("Do you want to send any file(y or n)?")


if (file_send=="y"):
	fileadress = str(raw_input("Enter the file address: "))
	filename = str(raw_input("Enter the file name: "))

	file=fileadress+"/"+filename
	with open(file, "rb") as attachment:
		part = MIMEBase("application", "octet-stream")
		part.set_payload(attachment.read())


	encoders.encode_base64(part)


	part.add_header(
    	"Content-Disposition",
    	"attachment; filename= "+filename+"",
					)


	message.attach(part)
	text = message.as_string()

else:
	text = message.as_string()



try:
	smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	password = str(getpass.getpass(prompt="enter your password: "))
	smtpObj.login(str(sender_email), str(password))
	smtpObj.sendmail(str(sender_email), str(receiver_email) , text)
	print("Mail sent!")
	smtpObj.quit()

except :
	print("Connection Issue")