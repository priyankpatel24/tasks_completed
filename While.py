# Start with asking users to enter a number

num_initial = int(input("Please input a number: "))
i = 0
sum_num = num_initial + i

# Adding in while function and an if function of when to stop

while num_initial != -1:
    next_num = int(input("Please input another number: " ))
    i += 1
    sum_num += next_num
    if num_initial == -1 or next_num == -1 :
        break

# Break added at sum of input. Now to print total and work out average

total = str(sum_num + 1)

print("The total of your numbers is " + total + ". Now we will calculate the average of your total. " )

# Add a calculation for the average and print the result

avg = int(total) / i

print ("The average of your numbers is " + str(avg))