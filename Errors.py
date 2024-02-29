# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")
print ("\n")

# Syntax error above as there was no parentheses
# Syntax error above as there was an indentation

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24"
age = int(age_str) 
print("I'm " + str(age) + " years old.")

# Syntax error above as there was an indentation
# Runtime error above as 'age_Str' is not defined because '==' was used instead of '='
# # Runtime error above as 'age_Str' does not need 'years old' at the end
# Runtime error above as 'age' has been changed into an integer and needs to be a string in order to print

# Variables declaring additional years and printing the total years of age
years_from_now = int(3)
total_years = age + years_from_now

# Syntax error above as there was an indentation

print ("The total number of years: " + "answer_years")

# Syntax error above as there was no parentheses

# Variable to calculate the total amount of months from the total amount of years and printing the result

total_months = total_years * 12
print ("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")

# Syntax error above as 'total' had not been defined and should have 'total_years'
# Syntax error above as there was no parentheses
# Error as total did not take into account adding 6 months

#HINT, 330 months is the correct answer