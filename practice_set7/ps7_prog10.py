text = input("Type something: ")
substring_value = input("Enter substring: ")

is_found = False

for index_position in range(len(text) - len(substring_value), -1, -1):
    if text[index_position:index_position + len(substring_value)] == substring_value:
        print(index_position)
        is_found = True
        break

if not is_found:
    print("Not found")