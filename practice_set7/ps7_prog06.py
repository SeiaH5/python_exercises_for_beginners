text = input("Type something: ")
total_width = int(input("Enter width: "))

space_count = total_width - len(text)

if space_count > 0:
    print(' ' * space_count + text)
else:
    print(text)