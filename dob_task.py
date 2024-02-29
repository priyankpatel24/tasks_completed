'''Task 14 - Date of Birth task'''
# Set names and dates empty lists
# Open file with r+
# Create for loop for names and dates using split by reading each line
# Print names first and then print dates.

names = []
dates = []

with open("dob.txt", "r+") as file:
    for line in file:
        names.append(line.split()[0:2])  # Loops through to append names
        dates.append(line.split()[2:])  # Loops through to append dates

print("Name") #  Print name first as the title, followed by each names
for name in names:
    print(" ".join(name))

print("\nBirthdate") #  Print Birthdate on a new line, as per task guidelines
for date in dates:
    print(" ".join(date))
