print('How many cats do you have?')
numCats = input()
try:
    if numCats[0] == '-':
        print('No negative numbers.')
    elif int(numCats) >= 4:
        print('You have many cats.')
    else:
        print('You don\'t have many cats.')
except ValueError:
    print('Please type an integer.')

