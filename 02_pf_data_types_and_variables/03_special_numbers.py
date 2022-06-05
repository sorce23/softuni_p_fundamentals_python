number = int(input())

for i in range(1, number + 1):
    sum_is_five_seven_eleven = False
    sum_left = i % 10
    sum_right = i // 10
    total_sum = sum_left + sum_right
    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        sum_is_five_seven_eleven = True
    if sum_is_five_seven_eleven:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
