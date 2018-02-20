import RPi.GPIO as GPIO
import time
import LCD&PIR.py


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)


        
    
    
while True:
    seth = 0#LED output pin
    GPIO.output(3, 0)
    GPIO.output(12, 0)
    while seth < 20:
        i = GPIO.input(11)#Turn OFF LED
        if i==1:
#            GPIO.output(3, 1)
#            GPIO.output(12, 1)#Turn ON LED
            seth +=1
            message()
#            print("Nice shot!")
#            time.sleep(2)
#            print("Your score is " + str(seth))
            time.sleep(8)
 #           GPIO.output(12, 0)
#            GPIO.output(3, 0)
            
            
        
           
        else:
            time.sleep(0.5)
        
            
    
        
                 
                 
             
       
