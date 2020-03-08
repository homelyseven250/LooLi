#All code copyright @gekepdp
###################################################################################################################
#STARTUP CODE
from random import *
import pickle
import fnmatch
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
        input_data = []
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
    global input_count
    global session_inputs
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
    input_count = 0
    session_inputs = []
    
def create_db_record():
    global session_id_counter
    global last_session_id_counter
    global session_id
    global session_file
    global session_file_address
    session_id_counter = open("./db/session_id_counter", "r")
    last_session_id_counter = session_id_counter.read(1)
    session_id_counter.close()
    session_id_counter = open("./db/session_id_counter", "w")
    session_id_counter.write(str(int(last_session_id_counter)+1))
    session_id_counter.close()
    session_id = int(last_session_id_counter)
    session_file_address = "./db/sessions/"+str(session_id)+".pkl"
    session_file = open(session_file_address, "wb")
    session_file.close()


def user_input():
    global last_input
    global input_data
    global input_count
    global session_inputs
    input_count += 1
    last_input = {"user_input":input() + " ", "pos":input_count}
    session_inputs.append(last_input)
    upload_input_data(last_input)
    analyse(last_input)
    

def upload_input_data(data_to_upload):
    global old_file
    global session_inputs
    input_data_file = open("input_data.pkl","rb")
    old_file = pickle.load(input_data_file)
    old_file.append(data_to_upload)
    input_data_file.close()
    input_data_file = open("input_data.pkl","wb")
    pickle.dump(old_file,input_data_file)
    input_data_file.close()
    session_file = open(session_file_address, "wb")
    pickle.dump(session_inputs, session_file)

def reply(request):
    print(request)
    user_input()
    
def change_str_char(request, letter, number):
    new = request[:number] + 'Z' + request[number+1:]
    return new

def analyse(request):
    word_start = 0
    for loop in range(0, len(old_file)):
        global input_only
        input_only = []
        input_only.append(old_file[loop]["user_input"])
    for x in old_file:
        letter_count = 0
        for y in x["user_input"]:
            letter_count+=1
            if y == " ":
                word = x["user_input"][int(word_start):letter_count]
                word_start = letter_count
                for word_count in range(0, len(request)):
                          wordaslist = []
                          wordaslist.append(change_str_char(request["user_input"], "*", word_count))
                for processing_word in wordaslist:
                    if fnmatch.filter(input_only, processing_word) != "":
                        reply(x["user_input"])
                                      
            
    
startup()
setvars()
create_db_record()
user_input()
#Next - add user input and basic GUI maybe!
        
