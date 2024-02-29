# Work in order of size, biggest to smallest condition
# Add 21st annd else at the end of all other elif
age = int(input("What is your age? " ))
if age > 100:
    print("Sorry, you're dead." )
elif age >= 65:
    print("Enjoy your retirement!" )
elif age >= 40 and age < 65:
    print("You're over the hill." )
elif age < 13:
    print("You qualify for the kiddie discount." )
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")