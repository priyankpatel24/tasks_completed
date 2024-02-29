# The pattern goes from 1 * to 5 * and back
# Number range should be 1 to 10 as their are 9 lines of *
# Define number of 8 to begin from 1
# Write code to go from 1 to 5, increasing number of *
# Write code to go from 6 to 10, decreasing number of *
# Combine the two lines of code within the same for loop

num = 1

# Write code for 1 * to 5 *

while num <= 5 :
    for num in range (1,10) :
        if num >= 6 :
            break
        else:
            print("*" * num)

# Ran code to verify it works. Now to write code from 6 to 10, decreasing number of *

if num >= 6 :
    for num in range (6, 10,) :
        print ("*" * ( 10 - num))

# Ran code to verify it works. Now to combine. This means if I run the code, it should show the pattern twice.

for num in range (1,10):
    if num <= 5 :
        print ("*" * num)
    else: 
        print ("*" * ( 10 - num ))

# Ran code to verify. Therefore pattern with one for loop is code from line 27 to 32.
