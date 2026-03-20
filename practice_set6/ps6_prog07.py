text = input("Type something: ")
total_width = int(input("Enter width: "))

total_spaces = total_width - len(text)

if total_spaces > 0:
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    print(' ' * left_spaces + text + ' ' * right_spaces)
else:
    print(text)