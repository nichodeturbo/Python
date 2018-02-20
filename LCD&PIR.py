seth = 1
def message():
    import time
    import Adafruit_CharLCD as LCD

    lcd_rs        = 25
    lcd_en        = 24
    lcd_d4        = 23
    lcd_d5        = 27
    lcd_d6        = 21
    lcd_d7        = 22
    lcd_backlight = 4

    lcd_columns = 16
    lcd_rows    = 2

    lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)


    lcd.message("Nice shot!")
    time.sleep(4)
    lcd.clear()
    lcd.message("Your score is " + str(seth))
    time.sleep(6)
    lcd.clear
    
def pir():
    import RPi.GPIO as GPIO
    import time


    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)

    while True:
        seth = 1
        #LED output pin
        GPIO.output(3, 0)
        GPIO.output(12, 0)
        while seth < 10:
            i = GPIO.input(11)#Turn OFF LED
            if i==1:
                GPIO.output(3, 1)
                GPIO.output(12, 1)#Turn ON LED
                seth += 1
                time.sleep(8)
                GPIO.output(12, 0)
                GPIO.output(3, 0)
                
            else:
                time.sleep(0.5)
            break
        break

