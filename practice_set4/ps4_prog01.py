numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
for items in numbers:
    if numbers.count(items) == 1:
        numbers.remove(items)
    else:
        print(items)