# Get input for score percentage
percentage = float(input("Enter your percentage: "))

# Check eligibility
if percentage > 70:
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    location = input("Enter your location: ")
    print("You are eligible.")
else:
    print("You are not eligible.")
