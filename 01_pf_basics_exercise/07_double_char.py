command = ''

while command != 'End':

    if command != 'SoftUni':
        print(''.join([char*2 for char in command]))
    command = input()
