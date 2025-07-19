# Check Type of Variable

# Take input from user
user_input = input("Enter something: ")

# Print the value and its type
print("You entered:", user_input)
print("Data type:", type(user_input))

# Digit Extractor

# Ask for a 3-digit number as input
num = input("Enter a 3-digit number: ")

# Check if it's exactly 3 digits
if len(num) == 3 and num.isdigit():
    print("The digits are:", num[0], num[1], num[2])
else:
    print("Please enter a valid 3-digit number.")
