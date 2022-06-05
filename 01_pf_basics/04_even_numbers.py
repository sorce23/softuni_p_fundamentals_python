# n = int(input())
# all_even = True
#
# for i in range(n):
#     current_number = int(input())
#     if current_number % 2 != 0:
#         print(f'{current_number} is odd!')
#         all_even = False
#         break
#
# if all_even:
#     print("All numbers are even.")

number_of_lines = int(input())

for _ in range(number_of_lines):
    current_number = int(input())

    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        break

else:
    print("All numbers are even.")
