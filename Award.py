# Set out criteria
# Set qualifying time to be 100 minutes
# input for each event
# calculate using sum and display using print
# Use logic operation to give out the award
quali = float (100)
swim = float (input("How  long in minutes did it take for you to complete the swimming event? " ))
cycle = float (input("How  long in minutes did it take for you to complete the cycling event? " ))
run = float (input("How  long in minutes did it take for you to complete the running event? " ))
total = (swim + cycle + run)
print("Your completion time for the triathlon was " + str(total ))
# total remains as a float so we can use it to determine qualifying
if total >= 111:
    print("Sorry, you did not receive an award." )
elif total >= 106 and total <=110:
    print("You have received a Provincial Scroll award." )
elif total >= 101 and total <= 105:
    print("You have received the Provincial Half Colours Award." )
else:
    print("Congrats! You have received the Provincial Colours Award!" )