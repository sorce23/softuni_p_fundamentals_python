name = input()
all_students_are_welcome = True
while name != 'Welcome!':

    if name == 'Voldemort':
        print('You must not speak of that name!')
        all_students_are_welcome = False
        break
    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    if len(name) == 5:
        print(f'{name} goes to Slytherin.')
    if len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    if len(name) > 6:
        print(f'{name} goes to Hufflepuff.')
    name = input()
if all_students_are_welcome:
    print('Welcome to Hogwarts.')
