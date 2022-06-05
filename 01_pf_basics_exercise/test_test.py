#
# funkciata enumerate()
#
# number = "SoftUni"
#
# # for current_digit in range(0, len(number)):
# #     if int(number[current_digit]) % 2 == 0:
# #         print(number[current_digit])
#
# for index, digit in enumerate(number):
#     print(index, digit)
#

# some_string = "Gosho6"
#
# for index, char in enumerate(some_string):
#     print(f'Index = {index} type of variable index = {type(index)}')
#     print(f'Char = {char} type of variable char = {type(char)}')

# slicing
#
# some_string = "Goshoepich"
# # new_string = ''
# # for char in range(len(some_string) - 1, - 1, -1):
# #     new_string += some_string[char]
# # print(new_string)
# # (start : end : step)
# print(some_string[1:5:2])

#endswith()   //  startswith()
#
# some_string = "https://softuni.bg/curriculum"
# if some_string.startswith('https'):
#     print("This site has SSL certificate.")
# else:
#     print("This site has NOT SSL certificate.")
