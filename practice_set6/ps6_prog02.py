text = input("Type something: ")
prefix_value = input("Enter prefix: ")

if text[:len(prefix_value)] == prefix_value:
    print(text[len(prefix_value):])
else:
    print(text)