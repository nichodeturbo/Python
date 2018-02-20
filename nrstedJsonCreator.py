#This will have the method for parsing a text file
#for parsing and creating a dictionary for word count.
#I need to figure out how to add another text files word dicitonary
#to the existing and then figure out how to do 100 at a time
#and how to simply create the json file at the end of the script and
#then upload into firebase
import re
import string
import json

print("What is the name of the file you would like to create? \n")          # "/Users/nichodeturbo/Desktop/dunno.txt"
userFileName = input()
helloPath = ("/Users/sethegger/Desktop/" + str(userFileName))
helloFile = open(helloPath, "w")

frequency3 = {}
document_text3 = open('/Users/sethegger/Desktop/biebs.txt', 'r')
text_string3 = document_text3.read().lower()
match_pattern3 = re.findall(r'\b[a-z]{3,15}\b', text_string3)

for word in match_pattern3:
    if word == "ansi":
        continue
    elif word == "fonttbl":
        continue
    elif word == "fnil":
        continue
    elif word == "helveticaneue":
        continue
    elif word == "csgray":
        continue
    elif word == "verdana":
        continue
    elif word == "colortbl":
        continue
    elif word == "cssrgb":
        continue
    elif word == "pard":
        continue
    else:
        count = frequency3.get(word,0)
        frequency3[word] = count + 1

frequency2 = {}
document_text2 = open('/Users/sethegger/Desktop/bieb2.txt', 'r')
text_string2 = document_text2.read().lower()
match_pattern2 = re.findall(r'\b[a-z]{3,15}\b', text_string2)

for word in match_pattern2:
    if word == "ansi":
        continue
    elif word == "fonttbl":
        continue
    elif word == "fnil":
        continue
    elif word == "helveticaneue":
        continue
    elif word == "csgray":
        continue
    elif word == "verdana":
        continue
    elif word == "colortbl":
        continue
    elif word == "cssrgb":
        continue
    elif word == "pard":
        continue
    else:
        count2 = frequency2.get(word,0)
        frequency2[word] = count + 1

frequency3_dump = json.dumps(frequency3)
frequency2_dump = json.dumps(frequency2)
helloFile.write(frequency3_dump)
helloFile.write(frequency2_dump)
