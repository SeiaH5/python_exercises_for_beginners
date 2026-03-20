text = input("Type something: ")
result_text = ""
is_new_word = True

for character in text:
    if character == ' ':
        result_text += character
        is_new_word = True
    else:
        if is_new_word:
            if 'a' <= character <= 'z':
                result_text += chr(ord(character) - 32)
            else:
                result_text += character
            is_new_word = False
        else:
            if 'A' <= character <= 'Z':
                result_text += chr(ord(character) + 32)
            else:
                result_text += character

print(result_text)