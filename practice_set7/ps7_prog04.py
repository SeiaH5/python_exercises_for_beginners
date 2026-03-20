text = input("Type something: ")
has_lowercase_letter = False

for character in text:
    if 'A' <= character <= 'Z':
        print(False)
        break
    if 'a' <= character <= 'z':
        has_lowercase_letter = True
else:
    print(has_lowercase_letter)