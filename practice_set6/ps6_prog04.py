text = input("Type something: ")
has_uppercase_letter = False

for character in text:
    if 'a' <= character <= 'z':
        print(False)
        break
    if 'A' <= character <= 'Z':
        has_uppercase_letter = True
else:
    print(has_uppercase_letter)