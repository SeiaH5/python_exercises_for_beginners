numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
for item in (set(numbers)):
    print(item)