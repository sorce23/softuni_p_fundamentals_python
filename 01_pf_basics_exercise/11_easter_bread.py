budget = float(input())
flour_price = float(input())
number_of_loaves = 0
colored_eggs = 0

eggs_price = flour_price * 0.75
milk_price = 1/4 * (flour_price + flour_price * 0.25)
budget_is_enough = True

while budget_is_enough:
    loaf = flour_price + eggs_price + milk_price
    if budget < loaf:
        budget_is_enough = False
        break
    budget -= loaf
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
