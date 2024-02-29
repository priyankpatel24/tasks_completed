import math

# Create the menu that users select at the start
# This menu should recognise different inputs for each selection and have an error message built in

print("Investment - to calculate the amount of interest you'll earn on your investment" )
print(" Bond - to calculate the amount you'll have to pay on a home loan" )

selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: " )

if selection == "bond" or selection == "Bond" or selection == "BOND":
    print("bond selected")
elif selection == "investment" or selection == "Investment" or selection == "INVESTMENT":
    print("investment selected")
else:
    print("Your selection is not on the menu above, please try again. " )

# Checked that the selection part is working without any errors.
# Now writing code for the investment input followed by the bond input

if selection == "investment" or selection == "Investment" or selection == "INVESTMENT":
    deposit = float(input("How much money are you depositing? " ))
    rate = float(input("What is the interest rate? " ))
    years = int(input("For how many years are you planning on investing? " ))

elif selection == "bond" or selection == "Bond" or selection == "BOND":
    value = float(input("What is the present value of the house? " ))
    int_rate = float(input("What is the interest rate? " ))
    months = float(input("How many months doing you plan on taking to repay the loan? " ))

# Checked the selection input is correct, now writing respective calculations

if selection == "investment" or selection == "Investment" or selection == "INVESTMENT":
    interest = input("Would you like simple or compound interest? " )

    if interest == "simple" or interest == "Simple" or interest == "SIMPLE":
        total = int(deposit * (1 + ((rate/100)*years)))
        print("This investment would yield £" + str(total))

    elif interest == "compound" or interest == "Compound" or interest == "COMPOUND":
        total = int(deposit * math.pow((1+(rate/100)),years))
        print("This investment would yield £" + str(total))

elif selection == "bond" or selection == "Bond" or selection == "BOND":
    repayment = int(((int_rate/1200) * value) / (1-(1+(int_rate/1200))**(-months)))
    print("Your monthly repayment amount will be £" + str(repayment) )
