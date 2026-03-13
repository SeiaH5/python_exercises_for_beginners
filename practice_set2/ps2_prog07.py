even = 0
for i in range(10):
    num = int(input("Please enter a number: "))
    if num % 2 == 0:
        even += 1
print(f"There are {even} even number/s.")