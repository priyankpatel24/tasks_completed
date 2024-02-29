# Establish a string
first_string = "I am learning how to code"

# Split the string into two lists for characters
# One list is for upper and the other list is for lower

up_words = first_string.upper()
low_words = first_string.lower()
up_words.split(" ")
low_words.split(" ")

print(up_words)
print(low_words)

# List now stored as a string. List cannot be upper or lower
# Establish the string as upper and lower case
# Then seperate words so they are ordered by even and odd index

even_char = up_words [0::2]
odd_char = low_words [1::2]

even_char.split()
odd_char.split()

print(even_char)


# Now merge the two lists so that the characters read as a sentence again

merged_char = zip(even_char,odd_char)
merged_list = print(list(merged_char))


# Split the string into two lists for words
# One list is for upper and the other list is for lower

caps = first_string.upper()
low = first_string.lower()
up_words = caps.split(" ")
low_words = low.split(" ")

# Now seperate words so they are ordered by even and odd index

even_index = up_words [0::2]
odd_index = low_words [1::2]

# Now merge the two lists so that the words read as a sentence again

merged_words = zip(even_index,odd_index)
print(list(merged_words))

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

