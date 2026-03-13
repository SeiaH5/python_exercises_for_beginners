numbers = []
while True:
    num = int(input("Please enter a number: "))
    if num not in numbers:
        print("Unique")
    else:
        print("Duplicate")
    numbers.append(num)
