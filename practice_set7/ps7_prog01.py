text = input("Type something: ")

index_position = len(text) - 1
while index_position >= 0 and text[index_position] == ' ':
    index_position -= 1

print(text[:index_position + 1])