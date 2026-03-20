text = input("Type something: ")
suffix_value = input("Enter suffix: ")

if text[-len(suffix_value):] == suffix_value:
    print(text[:-len(suffix_value)])
else:
    print(text)