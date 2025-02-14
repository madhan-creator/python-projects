# Print numbers divisible by 5 but not by 10
for num in range(1, 101):  # Adjust range as needed
    if num % 5 == 0 and num % 10 != 0:
        print(num)
