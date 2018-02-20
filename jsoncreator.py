import re
import string

frequency = {}
document_text = open('/Users/sethegger/Desktop/2016Top5.txt.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
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
        count = frequency.get(word,0)
        frequency[word] = count + 1


#frequency_list = frequency.keys() #don't need to see this

#for words in frequency_list:
    #print(words, frequency[words])

print(frequency)#this seems to be in json format already..
