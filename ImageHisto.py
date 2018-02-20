# draw histogram in python. 

from PIL import Image, ImageDraw
from collections import Counter
import time


whereFrom = input("Enter the file path you would like to open: \n")
im = Image.open(str(whereFrom))

pixelList = im.histogram(mask=None, extrema=None)

pixelDict = Counter(pixelList)

# print(pixelDict)
howMany = len(pixelList)
howManyBy4 = howMany / 4
howManyBy6 = howMany / 6

section1 = pixelList[:192]
section2 = pixelList[192: 385]
section3 = pixelList[385:578]
section4 = pixelList[578:768]

print("You have " + str(len(pixelList)) + " items in your list")
print("You have " + str(len(section1) + len(section2) + len(section3) + len(section4)) +
      " items in your list.")


def lets_go():
    thisRid = input("You want to see something ridiculous? \n")
    if thisRid == "yes":
        print(pixelList)
        print(section1)
        print(section2)
        print(section3)
        print(section4)
        for i in pixelList:
            if i % 5 == 0:
                print("I got " + str(i) + " problems")

        time.sleep(5)
        im.show()
        print("Goodbye!")
    else:
        print("Okay...bye.")
        exit()


lets_go()

# I want a function that take any integer representing a color over a specfic
# amount to make all those integers go down by 300
