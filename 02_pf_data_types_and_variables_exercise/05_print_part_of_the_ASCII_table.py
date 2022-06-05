start_index = int(input())
final_index = int(input())
final_string = ''
for character in range(start_index, final_index + 1):
    # print(chr(character), end= " ")
    final_string += chr(character) + " "
print(final_string)
# print(final_string.strip())
