import json

data1 = []
def add():
    while True:
        task = input("Entre the task:")

        data1.append({
            "tasks":[{
            "task":task,
            "Mode" : "Not complete"
            }
            ]
        })

        try:
            with open("to-do.json","r")as f:
                 data = json.load(f)

            data1.append({
            "tasks":[{
            "task":task,
            "Mode" : "Not complete"
            }
            ]
        })

        

            with open("to-do.json","w")as f:
                 json.dump(data1,f,indent = 3)
        
            query = input("Do you want to add another task:")
            if(query.lower() == "yes"):
               continue
            else:
               print("Greetings")
               break
        except:
            with open("to-do.json","w")as f:
                 json.dump(data1,f,indent = 3)
        query = input("Do you want to add another task:")
        if(query.lower() == "yes"):
               continue
        else:
               print("Greetings")
               break
            
        # data1.append({
        #     "tasks":[{
        #     "task":task,
        #     "Mode" : "Not complete"
        #     }
        #     ]
        # })

        

        # with open("to-do.json","w")as f:
        #     json.dump(data1,f,indent = 3)
        
        # query = input("Do you want to add another task:")
        # if(query.lower() == "yes"):
        #     continue
        # else:
        #     print("Greetings")
        #     break

    
ques = input("Which task you want to perform:")
if(ques.lower() == "add"):
    add()