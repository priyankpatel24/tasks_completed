# setup the write file
# input needed for number of students
# for loop equals that number 
# input each student ID number and the dotted line
# save all of these into a new text file

number = (input("How many students are registering?: " ))

with open ("reg_form.txt", 'w') as f:
    f.write("The number of students registering is " + str(number))

# inital file set, now to create for loop and append file

for i in range (int(number)):
    IDs = input("What is your student ID number? ")
    with open ("reg_form.txt", 'a') as f: 
        f.write("\n" + IDs + "   ..............................................." + "\n")

    
    

