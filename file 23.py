# Loop from 1 to 20 and stop if divisible by 7
for num in range(1, 21):
    print(num)
    if num % 7 == 0:
        break
3. Continuously ask for a number until a negative number is entered
python
Copy code
# Continuously ask the user to enter a number
while True:
    number = float(input("Enter a number: "))
    if number < 0:
        print("Negative number detected. Exiting loop.")
        break
