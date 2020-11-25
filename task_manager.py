#This is Compulsory Task 1 and Task 2
#program for task management 

# login
user_file = open("user.txt","r+")
login = False
admin = False
adm1n = False
admin_name = admin
admin_password = adm1n



#Asking the user for there credentials
while login == False:
    username = input("Enter your user name: ")
    password = input("Enter your user password: ")

    for line in user_file:
        
        valid_user = line.split(",")
        valid_password = valid_user[1].replace("\n","")
        valid_username = valid_user[0]
        

        if username == valid_username and password == valid_password:
            login = True
    

if login == False:
    print("Incorrect details! Please enter valid username and password ")
    user_file.seek(0)

print(login)
    
# Choice menu

choice = input('''
Please select one of the following options :
r  -  register user
a  -  add task
va -  view all tasks
vm -  view my tasks
e  -  exit 
''')

if choice == "r":
    task_file = open("tasks.txt","r")

    if choice == "ru":
        username = input("Please enter the user you would like to add : ")
        password = input("Enter your password")
    
        with open('user.txt', 'a+') as file:
            file.write(f"{username},{password}")

print ("Thank you, for adding a new user")




if choice == "a":
    task_file = open("tasks.txt","a+")
    # add task
    # format (admin, Assign initial tasks, Use taskManager.py to assign each team member with appropriate tasks, 10 Oct 2019, 25 Oct 2019, No)
    username = input(" Enter the user name the Task belongs to : ")
    task_name = input("Enter the name of the Task : ")
    start_date = input("Enter the starting date : ")
    end_date = input("Enter the due date : ")
    is_completed = input("is the task completed : ")

    task_file.write(f"\n{username}, {task_name}, {start_date}, {end_date}, {is_completed}")
    task_file.close()
    
    
  
elif choice == "va":
    # View all the tasks
    task_file = open("tasks.txt","r")

    for line in task_file:
        username, tasks_name, start_date, end_date, is_completed = line.split(", ")
        print(f'''
             Name         : {username}
             Task         : {tasks_name}
             Start Date   : {start_date}
             Due Date     : {end_date}
             Is compleded : {is_completed}
             ''')
        task_file.close()
    

elif choice == "vm":
    # View a certain user name tasks
    task_file = open("tasks.txt","r")

    for line in task_file:
       username, tasks_name, start_date, end_date, is_completed = line.split(", ")

       if username == username:
           print(f'''
             Name         : {username}
             Task         : {tasks_name}
             Start Date   : {start_date}
             Due Date     : {end_date}
             Is compleded : {is_completed}
             ''')
       task_file.close()
    

elif choice == "e":
    login= False
    # Exiting out of the file
    #if line in task_file:
        #task_file.close()


















    

    

