import json

def add():
    while True:
        flag = 1
        task1 = input("Entre the task:")

        with open("to-do.json","r")as f:
            data = json.load(f)
        
        try:
            i = data["todo"][-1]["id"] + 1
        except:
            i = 1

        for ln in data["todo"]:
            if(ln["task"].lower() == task1.lower()):
                print("The task already exists")
                flag = 0
                break
        if(flag == 0):
            que = input("Do you want to add another task:")
            if(que.lower() == "yes"):
                continue
            else:
                print("Greetings") 
                break      
        new_task = {
            "id":i,
            "task":task1,
            "status": "Not completed"
        }
        data["todo"].append(new_task)

        with open("to-do.json","w")as f:
             json.dump(data,f,indent = 3)
        print("Your task is added successfully")

        query = input("Do you want to add another task:")
        if(query.lower() == "yes"):
            continue
        else:
            print("Greetings")
            break

def view():
    with open("to-do.json","r")as f:
        data = json.load(f)
    for ln in data["todo"]:
        print(f"{ln["id"]}. {ln["task"]} -> {ln["mode"]}")

def change():
    while True:
        flag = 1
        que = input("Entre the task which is done:")
        with open("to-do.json","r")as f:
            data = json.load(f)

        for ln in data["todo"]:
            if(ln["task"].lower() == que.lower()):  
                ID = ln["id"]
                flag = 0
                qu = input("Do you want to delete the changed task:")
                if(qu.lower() == "yes"):
                    data["todo"].remove(ln)
                else:
                    ln["status"] = "completed"
                break
               
        if(flag == 1):
            print("The task does not exist")
            q = input("Do you want to change anything:")
            if(q.lower() == "yes"):
                continue
            else:
                print("Greetings")
                break
        for ln in data["todo"]:
            if(ln["id"]>ID):
                ln["id"] == ln["id"] - 1

        with open("to-do.json","w")as f:
            json.dump(data,f,indent = 3)

        q = input("Do you want to change anything:")
        if(q.lower() == "yes"):
                continue
        else:
                print("Greetings")
                break

ques = input("Which task you want to perform:")
if(ques.lower() == "add"):
    add()
elif(ques.lower() == "view"):
    view()
elif(ques.lower() == "change"):
    change()