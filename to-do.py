import json

data1 = []
def add():
    while True:
        task1 = input("Entre the task:")

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
            print(data)

            if(data != []):
                 for ln in data[0]["tasks"]:

                    line = data[0]["tasks"][0]["task"].split()
                    print(line)
                    res = ' '.join(line)
                    print(res)
                    if(task1.lower() == res.lower()):
                      print("Task already exists")
                      flag = 0
                      break

                 if(flag == 0):
                      que = input("Do you want to add task:")
                      if(que.lower() == "yes"): continue
                      else:
                        print("greetings")
                        break 
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
                   print("The task is added successfully")

            else: 
                  print("Else is working at this time")
                  with open("to-do.json","w")as f:
                     json.dump(data1,f,indent = 3) 
                  print("The task is added successfully")

        except:
            with open("to-do.json","w")as f:
                 json.dump(data1,f,indent = 3)
            print("The task is added successfully")


        query = input("Do you want to add another task:")
        if(query.lower() == "yes"):
               continue
        else:
               print("Greetings")
               break
    
ques = input("Which task you want to perform:")
if(ques.lower() == "add"):
    add()