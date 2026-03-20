text = input("Type something: ")

if text == "":
    print(text)
else:
    result_text = ""

    first_character = text[0]
    if 'a' <= first_character <= 'z':
        result_text += chr(ord(first_character) - 32)
    else:
        result_text += first_character

    for character in text[1:]:
        if 'A' <= character <= 'Z':
            result_text += chr(ord(character) + 32)
        else:
            result_text += character

    print(result_text)