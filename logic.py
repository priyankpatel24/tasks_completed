# create a creative logical error
# using the base of a previous task with a 'while' loop

num_initial = int(input("Please input a number: "))
i = 1
sum_num = num_initial + i

while num_initial != -1:
    next_num = int(input("Please input another number: " ))
    sum_num += next_num
    i = sum_num # This is the incorrect formula
    if num_initial == -1 or next_num == -1 :
        break

total = str(sum_num + 1)

print("The total of your numbers is " + total + ". Now we will calculate the average of your total. " )

avg = int(total) / i # the formula works but will not be numerically correct

# If the loop works but results in the wrong average, that means a logical error has been successfully created

print ("The average of your numbers is " + str(avg))