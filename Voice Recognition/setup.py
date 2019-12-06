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

def loadTemplates():
    template1 = AudioSegment.from_file("./Dataset/Template/0a7c2a8d_nohash_0.wav")  # female yes
    template2 = AudioSegment.from_file("./Dataset/Template/0b40aa8e_nohash_0.wav")  # female no
    template3 = AudioSegment.from_file("./Dataset/Template/0135f3f2_nohash_0.wav")  # male yes
    template4 = AudioSegment.from_file("./Dataset/Template/0b56bcfe_nohash_0.wav")  # male no
    return template1, template2, template3, template4