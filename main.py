#All code copyright @gekepdp
###################################################################################################################
#STARTUP CODE
from random import *
#set previous_startup to FALSE until files are implemented
def startup():
    userfile = open("user.txt", "r")
    if userfile.read() != "blank":
        #file will come predone with the contents "blank"
        userfile.close()
        welcome(True)
    else:
        userfile.close()
        userfile = open("user.txt", "w")
        userfile.write("userfile")
        userfile.close()
        welcome(False)
def welcome(previous_startup):
    if previous_startup == True:
        print("Hello, it looks like you've previously used LooLi, so let's get started!")
    else:
        global name
        name = input("What's your name? (Not a nickname) ")
        userfile = open("user.txt", "a")
        userfile.write("\n" + name)
        nickname = input ("If you have a nickname, type it. Otherwise type No ")
        if nickname != "No":
            userfile.write("\n" + "True")
            userfile.write("\n" + nickname)
        else:
            userfile.write("\n" + "False")
        userfile.close()

##################################################################################################################

def setvars():
    global name
    global hasnickname
    global nickname
    userfile = open("user.txt", "r")
    userfile.readline()
    name = userfile.readline()
    name = name[:-1]
    if userfile.readline() == "True\n":
        hasnickname = True
        nickname = userfile.readline()
        #nickname = nickname[:-1]
    else:
        hasnickname = False
    userfile.close()
    
startup()
setvars()
#Next - add user input and basic GUI maybe!
        
