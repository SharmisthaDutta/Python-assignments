import json
#collection =dict()

def save_in_file(collection):
    
    try:
        f=open("birthday_informations.txt","w")
    except FileNotFoundError:
        print("sorry I could not open the file")
    else:
        json.dump(collection,f)


    
user_input='abc'

try:
    with open('birthday_informations.txt','r') as pick:
        print("yes I can open the file")
        pickle_file ={}
        pickle_file = json.load(pick)

except FileNotFoundError:
        print("sorry I could not open the file.. thats why i am creating one")
        pickle_file ={}
else:

    #pickle_file = json.load(pick)
        print("here you go")

while user_input!='':
    
    ''' enter you name here'''
    name =input("Enter a name:(blank to quit):")
    
    if name=='':
        break
    elif name in pickle_file:
        print("here is the information")
        print("%s's birthday is on %s" %(name,pickle_file[name]))
    else:
        print("I do not have information for %s" %name)
        print("what is his/her birthday")
        birthday = input()
        pickle_file[name]=birthday
save_in_file(pickle_file)
        
#fo = open("birthday_informations.txt", "w")
#json.dump(pickle_file,fo)
    

    
