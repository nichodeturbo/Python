import os
def begin():
    wouldYou = input("Would you like to create a new Directory and add some blank file!?\n Y or N ?")
    if wouldYou == "Y":
        directoryCreator()
    else:
        print("Viddy well then")
        exit()

def fileCreator():
    print("What is the name of the file you would like to create? \n") #Create a loop so they can add multiple files         # "/Users/nichodeturbo/Desktop/dunno.txt"
    userFileName = input()
    helloPath = (str(userFileName))
    helloFile = open(helloPath, "w")

def directoryCreator():
    print("What is the name of the directory you would like to create? \n")          # "/Users/nichodeturbo/Desktop/dunno.txt"
    userFolderName = input() #Make it choose folder enabled
    here1 = os.chdir("/Users/sethegger/Desktop/")#this changes directory to whatever we want
    os.mkdir(userFolderName)
    here2 = os.chdir("/Users/sethegger/Desktop/"+ str(userFolderName))
    #here#This creates a directory (folder) This name can be created by the user by an unput method
    while chris is True:
        shallWeMakeFile = input("Would you like to add files to this directory?\n Y or N ?")
        if shallWeMakeFile == "Y":
            fileCreator()
            chris = =False
        else:
            print("Goodbye!")
            exit()

begin()
