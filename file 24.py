# Continuously ask the user to enter a number
while True:
    number = float(input("Enter a number: "))
    if number < 0:
        print("Negative number detected. Exiting loop.")
        break
