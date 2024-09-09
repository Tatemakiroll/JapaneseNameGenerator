def main():
    global mode
    print("")
    print("          Japanese Name Generator")
    print("")
    print("----------------------------------------------")
    print("Mode")
    print("1.all mode")
    print("2.dot (ex. yamada.taro)")
    print("3.under score (ex. yamada_taro)")
    print("4.hyphen (ex. yamada-taro)")
    print("----------------------------------------------")
    mode = input("select mode: ")

def fileread():
    # read name
    print("Reading File")
    global full_names
    global full_names_rev
    with open("firstnames.txt", "r", encoding="utf-8") as f:
        first_names = [line.strip() for line in f.readlines()]
    with open("lastnames.txt", "r", encoding="utf-8") as f:
        last_names = [line.strip() for line in f.readlines()]
    full_names = [f"{last} {first}" for last in last_names for first in first_names]
    full_names_rev = [f"{first} {last}" for last in last_names for first in first_names]

def add():
    print("Generating name")
    global username
    username=[]
    if mode == "2":
        for i in full_names:
            username.append(i.replace(' ',"."))
            username.append(i[1]+"."+i.split()[1])
            username.append(i[0:2]+"."+i.split()[1])
            username.append(i.split()[0]+"."+i.split()[1][1])
            username.append(i.split()[0]+"."+i.split()[1][0:2])
        for i in full_names_rev:
            username.append(i.replace(' ',"."))
            username.append(i[1]+"."+i.split()[1])
            username.append(i[0:2]+"."+i.split()[1])
            username.append(i.split()[0]+"."+i.split()[1][1])
            username.append(i.split()[0]+"."+i.split()[1][0:2])
        for i in username:
            with open("output/japanese_userlist.txt", "a") as f:
                f.write(i+'\n')
    elif mode == "3":
        for i in full_names:
            username.append(i.replace(' ',"_"))
            username.append(i[1]+"_"+i.split()[1])
            username.append(i[0:2]+"_"+i.split()[1])
            username.append(i.split()[0]+"_"+i.split()[1][1])
            username.append(i.split()[0]+"_"+i.split()[1][0:2])        
        for i in full_names_rev:
            username.append(i.replace(' ',"_"))
            username.append(i[1]+"_"+i.split()[1])
            username.append(i[0:2]+"_"+i.split()[1])
            username.append(i.split()[0]+"_"+i.split()[1][1])
            username.append(i.split()[0]+"_"+i.split()[1][0:2]) 
        for i in username:
            with open("output/japanese_userlist.txt", "a") as f:
                f.write(i+'\n')
    elif mode == "4":
        for i in full_names:
            username.append(i.replace(' ',"-"))
            username.append(i[1]+"-"+i.split()[1])
            username.append(i[0:2]+"-"+i.split()[1])
            username.append(i.split()[0]+"-"+i.split()[1][1])
            username.append(i.split()[0]+"-"+i.split()[1][0:2])        
        for i in full_names_rev:
            username.append(i.replace(' ',"-"))
            username.append(i[1]+"-"+i.split()[1])
            username.append(i[0:2]+"-"+i.split()[1])
            username.append(i.split()[0]+"-"+i.split()[1][1])
            username.append(i.split()[0]+"-"+i.split()[1][0:2])  
        for i in username:
            with open("output/japanese_userlist.txt", "a") as f:
                f.write(i+'\n')
    else:
        for i in full_names:
            username.append(i.replace(' ',"."))
            username.append(i[1]+"."+i.split()[1])
            username.append(i[0:2]+"."+i.split()[1])
            username.append(i.split()[0]+"."+i.split()[1][1])
            username.append(i.split()[0]+"."+i.split()[1][0:2])        
        for i in full_names_rev:
            username.append(i.replace(' ',"."))
            username.append(i[1]+"."+i.split()[1])
            username.append(i[0:2]+"."+i.split()[1])
            username.append(i.split()[0]+"."+i.split()[1][1])
            username.append(i.split()[0]+"."+i.split()[1][0:2]) 
        for i in full_names:
            username.append(i.replace(' ',"_"))
            username.append(i[1]+"_"+i.split()[1])
            username.append(i[0:2]+"_"+i.split()[1])
            username.append(i.split()[0]+"_"+i.split()[1][1])
            username.append(i.split()[0]+"_"+i.split()[1][0:2])        
        for i in full_names_rev:
            username.append(i.replace(' ',"_"))
            username.append(i[1]+"_"+i.split()[1])
            username.append(i[0:2]+"_"+i.split()[1])
            username.append(i.split()[0]+"_"+i.split()[1][1])
            username.append(i.split()[0]+"_"+i.split()[1][0:2]) 
        for i in full_names:
            username.append(i.replace(' ',"-"))
            username.append(i[1]+"-"+i.split()[1])
            username.append(i[0:2]+"-"+i.split()[1])
            username.append(i.split()[0]+"-"+i.split()[1][1])
            username.append(i.split()[0]+"-"+i.split()[1][0:2])        
        for i in full_names_rev:
            username.append(i.replace(' ',"-"))
            username.append(i[1]+"-"+i.split()[1])
            username.append(i[0:2]+"-"+i.split()[1])
            username.append(i.split()[0]+"-"+i.split()[1][1])
            username.append(i.split()[0]+"-"+i.split()[1][0:2])
        for i in username:
            with open("output/japanese_userlist.txt", "a") as f:
                f.write(i+'\n')   
    print("Successfully Created Jananese Usernames")  
              
main()
fileread()
add()