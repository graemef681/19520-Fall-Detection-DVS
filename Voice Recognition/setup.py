from pydub import AudioSegment
name = ""
phoneNumber = ""


def getDetails():
    #ask for name
    print("Please enter the contact's name:")
    name = str(input())

    #ask for phoneNumber
    print("Please enter the contact's phoneNumber:")
    phoneNumber = str(input())

    #Write details to file to load in future
    f = open("./details.txt","w+")
    f.write(name + " \n")
    f.write(phoneNumber)

    return name, phoneNumber

def importDetails():
    #import previously saved details from file
    f = open("./details.txt", "r")
    contents = f.readlines()
    count=1
    for line in contents:
        if count==1:
            name=line
        elif count==2:
            phoneNumber=line
        count=count+1
    return name, phoneNumber

def displayContact():
    print("Contact name: ", name)
    print("Contact number: ", phoneNumber)
    return
