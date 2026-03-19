numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        if num not in numbers:
            numbers.append(num)
    except ValueError:
        break
print(*numbers)