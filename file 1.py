# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is divisible by both 3 and 5
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by 3 and 5.")
else:
    print("The number is not divisible by 3 and 5.")
