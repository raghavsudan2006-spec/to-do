import json

data1 = []
def add():
    while True:
        task1 = input("Entre the task:")
        print(data1)

        data1.append({
            "tasks":[{
            "task":task1,
            "Mode" : "Not complete"
            }
            ]
        })

        try:
            flag = 1
            with open("to-do.json","r")as f:
                data = json.load(f)

            if(data != []):
                 for ln in data[0]["tasks"][0]["task"]:
                    if(task1.lower() == ln.lower()):
                      print("Task already exists")
                      flag =0
                 if(flag == 0):
                      continue
                 else:
                   data1.clear()
                   data1.append(data)
                   data1.append({
            "tasks":[{
            "task":task1,
            "Mode" : "Not complete"
            }
            ]
        })                    
                   with open("to-do.json","w")as f:
                       json.dump(data1,f,indent = 3) 

            else: 
                  with open("to-do.json","w")as f:
                     json.dump(data1,f,indent = 3) 

        except:
            with open("to-do.json","w")as f:
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