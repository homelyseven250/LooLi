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
    all_text = []
    
def create_db_record():
    global session_id_counter
    global last_session_id_counter
    global session_id
    global session_file
    global session_file_address
    global all_inputs
    global all_inputs_list
    all_inputs_list = []
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
    all_text_file = open("./db/sessions/alltexts"+str(session_id)+".pkl", "wb")
    pickle.dump([],all_text_file)
    all_text_file.close()
    print("SESSION ID: "+str(session_id))


def user_input():
    global all_inputs_file
    global last_input
    global input_data
    global input_count
    global session_inputs
    global session_input_counter
    global all_inputs_list
    input_count += 1
    last_input = {"user_input":input() + " ", "pos":input_count}
    all_inputs_list.append(last_input["user_input"])
    session_inputs.append(last_input)
    upload_input_data(last_input)
    analyse(last_input)
    

def upload_input_data(data_to_upload):
    global old_file
    global session_inputs
    global all_inputs_list
    global alll_inputs_file
    input_data_file = open("input_data.pkl","rb")
    old_file = pickle.load(input_data_file)
    old_file.append(data_to_upload)
    input_data_file.close()
    input_data_file = open("input_data.pkl","wb")
    pickle.dump(old_file,input_data_file)
    input_data_file.close()
    session_file = open(session_file_address, "wb")
    pickle.dump(session_inputs, session_file)
    all_inputs_file = open("./db/datasets/all_inputs.pkl", "rb")
    all_inputs_list = pickle.load(all_inputs_file)
    all_inputs_file.close()
    all_inputs_list.append(data_to_upload["user_input"])
    all_inputs_file = open("./db/datasets/all_inputs.pkl", "wb")
    pickle.dump(all_inputs_list,all_inputs_file)
    all_inputs_file.close()

def all_text_add():
    global all_inputs_file
    global all_inputs_list
    all_inputs_file = open("./db/sessions/alltexts"+str(session_id)+".pkl", "rb")
    all_inputs_file.close()
    all_inputs_file = open("./db/sessions/alltexts"+str(session_id)+".pkl", "wb")
    pickle.dump(all_inputs_list, all_inputs_file)
    all_inputs_file.close()

def reply(request):
    global all_inputs_list
    all_inputs_list.append(request)
    all_text_add()
    print(request)
    user_input()
    
def change_str_char(request, letter, number):
    new = request[:number] + 'Z' + request[number+1:]
    return new

def analyse(request):
    global all_inputs_list
    ### V2 V2 V2 V2 ###
    letter_count = 0
    word_start = 0
    for x in all_inputs_list:
        current_processing = []
        for y in x:
            letter_count+=1
            if y == " ":
                current_processing.append(x[word_start:letter_count])
        for z in current_processing:
            if z in request["user_input"]:
                reply(all_inputs_list[all_inputs_list.index(x)+1])
            
                
    
                        
                                      
            
    
startup()
setvars()
create_db_record()
user_input()
#Next - add user input and basic GUI maybe!
        
