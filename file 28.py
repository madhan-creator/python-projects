# Loop from 1 to 20 and print all numbers except those divisible by 3
for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num)
