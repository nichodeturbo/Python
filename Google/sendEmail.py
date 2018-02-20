import smtplib
server = smtplib.SMTP("smtp.gmail.com:587")  #This is it...The holy grail my friend. I need to to be very careful though
server.starttls()                            #so nobody starts sending messages out with it other than my raspberryPi
server.ehlo()
server.login("EMAIL", "APIKEY")

msg = "Hello there from you python script and soon to be RaspberryPi!"
server.sendmail("EMAIL", "TO ADDRESS", msg)
server.quit()   # add this to PIR function on pi and copy the script into here and my raspberry respository
