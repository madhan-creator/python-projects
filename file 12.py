# Print first n prime numbers
n = int(input("Enter the number of prime numbers to print: "))
count, num = 0, 2

print("First", n, "prime numbers:")
while count < n:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1
