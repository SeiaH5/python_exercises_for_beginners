text = input("Type something: ")
converted_text = ""

for character in text:
    if 'A' <= character <= 'Z':
        converted_text += chr(ord(character) + 32)
    else:
        converted_text += character

print(converted_text)