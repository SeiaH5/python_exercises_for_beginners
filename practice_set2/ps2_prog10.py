num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
for i in range(num_1, num_2 + 1) or range(num_2, num_1 + 1):
    print(i)