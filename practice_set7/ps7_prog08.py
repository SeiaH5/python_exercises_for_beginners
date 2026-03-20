text = input("Type something: ")
substring_value = input("Enter substring: ")

occurrence_count = 0

for index_position in range(len(text) - len(substring_value) + 1):
    if text[index_position:index_position + len(substring_value)] == substring_value:
        occurrence_count += 1

print(occurrence_count)