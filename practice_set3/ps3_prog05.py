try:
    numbers = []
    while True:
        num = int(input("Enter a number: "))
        numbers.append(num)
except ValueError:
    print(*sorted(numbers))