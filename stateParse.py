import tkinter as tk
from tkinter import filedialog
import openpyxl
import datetime
from tkinter import messagebox


now = datetime.datetime.now()
today = (str(now.month) + str(now.day) + str(now.year))

root = tk.Tk()
root.withdraw()


bigCount = 0

messagebox.showinfo("Choose File", "Choose File To Sift Through.")
file_path = filedialog.askopenfilename()
helloFile = open(file_path, "r")


this_emptyList = []


def thisIsPerfect():
    userFileName = today
    helloPath3 = ("/Users/sethegger/Desktop/StateReport-/Identifiers/" + str(now) + ".txt")
    helloFile3 = open(helloPath3, "w")# This is our function that opens a specific text file and then searches through it for Identifierss
    with open(file_path) as f:
        for line in f:
            if str(line[0:10]) != " ":   ###THIS WILL CHANGE WHEN THE EXPORT BATCH FILE CHANGES
                this_emptyList.append(line[10:19])
                helloFile3.write(line[10:19] + "\n")#<<<<<<<<<      With this and userFileName commented, the program doesnt create and write to a new file....
            elif str(line[0:10]) == " ":
                continue
            else:
                break
        print(len(this_emptyList))
        helloFile3.close()
        exit()
        



while True:                     # Now my state reporting has a choose file on top of it
    thisIsPerfect()                # which has some huge implications
    break

