import json

data1 = []
def add():
    while True:
        task = input("Entre the task:")

        print(data1)
        data1.append({
            "task":task,
            "Mode" : "Not complete"
        })
        with open("to-do.json","a")as f:
            json.dump(data1,f,indent = 3)

        query = input("Do you want to add another task:")
        if(query.lower() == "yes"):
            continue
        else:
            print("Greetings")
            break

    
ques = input("Which task you want to perform:")
if(ques.lower() == "add"):
    add()