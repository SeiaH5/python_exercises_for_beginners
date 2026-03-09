odd = 0
for i in range(10):
    num = int(input("Please enter a number: "))
    if num % 2 == 1:
        odd += 1
print(f"There are {odd} odd number/s.")