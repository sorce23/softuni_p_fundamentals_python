budget = int(input())
budget_is_enough = True
command = input()

while command != 'End':
    current_product = int(command)
    if budget < current_product:
        print('You went in overdraft!')
        budget_is_enough = False
        break
    budget -= current_product
    command = input()

if budget_is_enough:
    print("You bought everything needed.")
