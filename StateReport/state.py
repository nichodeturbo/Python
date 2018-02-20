import tkinter as tk
from tkinter import filedialog
import openpyxl
import datetime
from tkinter import messagebox
import io
import os

now = datetime.datetime.now()
today = (str(now.month) + str(now.day) + str(now.year))

root = tk.Tk()
root.withdraw()
#user_input = input("File name?\n")
#userFileName = today
helloPath3 = ("/Users/sethegger/Desktop/StateReport-/NewReport/" + str(now) + ".txt")
helloFile3 = open(helloPath3, "w")
bigCount = 0

messagebox.showinfo("Choose File", "Choose File To Sift Through.")
file_path = filedialog.askopenfilename()
helloFile = open(file_path, "r")

messagebox.showinfo("Choose File", "Choose File Containing Identifiers.")
file_path2 = filedialog.askopenfilename()
helloFile2 = open(file_path2, "r")


empty_list = []

def thisIsCool():                    # This is our function that opens a specific text file and then searches through it for Identifierss
    with open(file_path) as f:
        for line in f:
            for i in empty_list:
                if str(i) != str(line[10:19]):
                    continue
                elif str(i) == str(line[10:19]):
                    print(line)
                    helloFile3.write(line)
                    continue
                else:
                    break
            helloFile3.close()

with helloFile2 as h:
    for line in h:
        if line != " ":
            line = line[0:9]
            empty_list.append(line)
        else:
            continue


thisIsCool()

exit()
