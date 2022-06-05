# number = int(input())
#
# for i in range(0, number + 1):
#     for j in range(0, i):
#         print('*', end='')
#     print()
# for i in reversed(range(0, number)):
#     for j in reversed(range(0, i)):
#         print('*', end='')
#     print()

number_of_stars = int(input())

for i in range(1, number_of_stars + 1):
    print(i * '*')

for i in range(number_of_stars - 1, 0, -1):
    print(i * '*')
