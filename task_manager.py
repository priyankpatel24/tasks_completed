# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w+") as default_file:
        pass

else:
    with open("tasks.txt", 'r+') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

#rewrote the above to include an else statement before the 'with' function.
        
task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component 
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
#This code reads usernames and password from the user.txt file
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

def reg_user(): #  Adds a new user to 'user.txt' and display error if user already exists
    '''used the register a new user and check if name already exists'''
    while True:
        new_username = input("New Username: ")
        if new_username in username_password:
            print("That user already exists, please try again: ")
            break
        # - Request input of a new password
        new_password = input("New Password: ")
        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")
        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))
            break

        #  - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

def add_task(): #  Adds a task and assigns it to a user
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")

        # Then get the current date.
        curr_date = date.today()
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")
        return


def view_all(): #  View all tasks
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine(): #  View tasks for the user that is logged in
    count = 0
    for t in task_list:
        if t['username'] == curr_user:
            count +=1
            disp_str = f"Task: {count} \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
        vm_selection = input("What task would you like to select: " )
        if vm_selection == "-1":
            return
        edit_option = input ("Enter C to mark as complete or E to edit task: " )
        #  Different input for selection of edit or complete
        if edit_option == "C" or edit_option == "c":
            selected_task = task_list[int(vm_selection)-1]
            if selected_task['completed'] == "True": # Cannot mark if complete
                print("The task has already been completed")
                return
            else:
                selected_task["completed"] = "True"
        if edit_option == "E" or edit_option == "e":
            selected_task = task_list[int(vm_selection)-1]
            if selected_task['completed'] == "True": #  Cannot edit if complete
                print("The task has already been completed")
                return
            else:
                #  Different input to edit date or user
                edit_selection = input ("Enter D to edit date or U to edit user: " )
                if edit_selection == "D" or edit_selection == "d":
                    new_date = input("Enter new date in following format 'YYYY-MM-DD': ")
                    selected_task["due_date"] = (new_date)
                    return
                if edit_selection == "U" or edit_selection == "u":
                    new_user = input("Enter the new user to assign this task to: ")
                    selected_task["username"] = (new_user)
                    return

def gen_rep():
    while True:
        with open("task_overview.txt", "w") as task_o:
            num_tasks = len(task_list)
            comp_t = 0
            incomplete = 0
            overdue = 0
            current_date = datetime.today()
            for key_word in task_list:
                if key_word['completed']: #  Checks complete
                    comp_t += 1
                else:
                    if key_word['due_date'] < current_date: #  If incomplete, also check date for overdue
                        overdue += 1
                    incomplete += 1 
                total_tasks = comp_t + incomplete #  Total tasks to calculate percentage
                comp_per = (comp_t / total_tasks)* 100
                incomp_per = (incomplete / total_tasks)* 100
            task_o.write(f"The total number of tasks is {num_tasks}\n")
            task_o.write(f"The number of incomplete tasks is {incomplete}\n")
            task_o.write(f"The number of complete tasks is {comp_t}\n")
            task_o.write(f"The number of overdue tasks is {overdue}\n")
            task_o.write(f"The percentage of completed tasks is {comp_per}%\n")
            task_o.write(f"The percentage of incomplete tasks is {incomp_per}%\n")  
        with open("task_overview.txt", "r") as task_read:   
            for line in task_read:
                print(line)
        with open("user_overview.txt", "w") as user_o:
            num_users = len(username_password)
            print(f"The total number of users is {num_users}")
            print(f"The total number of tasks is {num_tasks}")
            for current_user in username_password:
                curr_tasks = 0
                curr_complete = 0
                curr_incomplete = 0
                curr_overdue = 0
                current_date = datetime.today()
                for task in task_list:
                    if task["username"] == current_user:
                        curr_tasks += 1
                        if task["completed"]:
                            curr_complete += 1
                        else:
                            if task['due_date'] < current_date:
                                curr_overdue += 1
                            curr_incomplete += 1
                        sum_user_tasks = curr_complete + curr_incomplete
                        user_complete = (curr_complete / sum_user_tasks)* 100
                        user_incomplete = (curr_incomplete / sum_user_tasks)* 100
                user_o.write(f"The number of tasks assigned to {current_user} is {curr_tasks}\n")
                user_o.write(f"The number of incomplete tasks for {current_user} is {curr_incomplete}\n")
                user_o.write(f"The number of tasks completed by {current_user} is {curr_complete}\n")
                user_o.write(f"The number of overdue tasks assigned to {current_user} is {curr_overdue}\n")
                user_o.write(f"{current_user} has completed {user_complete}% of their tasks\n")
                user_o.write(f"{current_user} still has {user_incomplete}% of their tasks left to complete\n")
            with open("user_overview.txt", "r") as task_read:
                for line in task_read:
                    print(line)
        return  


def dis_stats():
    with open("tasks.txt", "w+") as tasks_read:
        for line in tasks_read:
            print(line)
    with open("user.txt", "w+") as users_read:
        for line in users_read:
            print(line)

while True:
    # presenting the menu to the user
    menu = input('''Please select one of the following options:
r - registering a user
a - adding a task
va - view all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - exit
: ''')
    if menu == "r" or menu == "R":
        reg_user()
    elif menu == "a" or menu == "A":
        add_task()
    elif menu == "va" or menu == "VA":
        view_all()
    elif menu == "vm" or menu == "VM":
        view_mine()
    elif menu == "gr" or menu == "GR":
        gen_rep()
    elif menu == "ds" or menu == "DS":
        dis_stats()
    elif menu == "e" or menu == "E":
        print("Goodbye!!!")
        exit()
    else:
        print("You have made a wrong choice, Please Try again")