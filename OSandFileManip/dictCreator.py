def doThisStuff():
    x = {}
    lyricFile = input("past the path of the file you want to read\n")
    document_text = open(lyricFile, 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
    for word in x: # I need to make this into a resuable functions and make the lists
        if word == "ansi":      #and dicts create and be anem through 100 from a function as well
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
            count = x.get(word,0)
            x[word] = count + 1
    return(x)
doThisStuff()
print(x)
