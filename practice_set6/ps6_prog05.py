text = input("Type something: ")
suffix_value = input("Enter suffix: ")

if len(suffix_value) <= len(text) and text[-len(suffix_value):] == suffix_value:
    print(True)
else:
    print(False)