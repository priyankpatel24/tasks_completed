# Turn the input into a string first
# Use a for or while loop instead
# You don’t need to use the split function for the first part of the task, only the second part task
# This is because the second part needs to use the spaces to recognise when to change
# To access each word  or character, you need to use the modulus operator --
# with an ifelse statement that alternatives either odd or even and then upper or lower
# If the length changes, this would now work
# for loop would be a set number of loops and while loops would be a varying number
# If using a for loop, use the ‘len’ function to get the length of the string entered by the user
# Would NOT recommend using zip
# Create an empty list before the for loop and then append with upper or lower.
# This makes it easier so that once finished, join together

user_string = input ("Please enter sentence:")

SENTENCE = ""
for char in range(len(user_string)):
    if char % 2 == 0:
        SENTENCE += user_string[char].upper()
    else:
        SENTENCE +=user_string[char].lower()

print (f"Your sentence as alternating characters is: {SENTENCE}")



