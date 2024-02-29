### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

# --- Lists --- #
# Initialise an empty list to store the email objects.

# --- Functions --- #
# Build out the required functions for your program.

class Email(): 

    #  Class variables
    has_been_read = False #  Default email has not been read yet

    def __init__(self, index, email_address, subject_line, email_content, inbox):
        self.index = index
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.inbox = inbox

    def mark_as_read(self): #  Marks email as read
        self.has_been_read = True
    

    def populate_inbox(self):
        email_object = self.email_address + self.subject_line + self.email_content
        print(f"The email object is {email_object}")
        self.inbox =[email_object]

    # Create 3 sample emails and add it to the Inbox list. 

    def list_emails(self):
        for self.subject_line in self.inbox:
            print(self.subject_line + self.index)
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.

    def read_email(self):
        self.has_been_read = True


    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        
    elif user_choice == 2:
        # add logic here to view unread emails
            
    elif user_choice == 3:
        # add logic here to quit appplication

    else:
        print("Oops - incorrect input.")

