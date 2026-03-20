text = input("Type something: ")
total_width = int(input("Enter width: "))

zero_count = total_width - len(text)

if zero_count > 0:
    print('0' * zero_count + text)
else:
    print(text)