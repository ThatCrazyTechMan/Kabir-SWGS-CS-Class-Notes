
film = 'avengers endgame'
obfuscated = ''
for letter in film:
    if letter == ' ':
        obfuscated += '/'
    else:
        obfuscated += '_'
obfuscated_array = []
for letter in obfuscated:
    obfuscated_array.append(letter)
film_array = []
for letter in film:
    film_array.append(letter)

remaining_guesses = 5

print(obfuscated)

gameOver = False
while not gameOver:
    choice = input('Enter a letter or a film: ')
    if choice == film:
        print('You won!!!')
        break
    for i in range(0, len(obfuscated_array)):
        if film_array[i] == choice:
            obfuscated_array[i] = film_array[i]

    if choice not in film_array:
        remaining_guesses -= 1
        print(f'{remaining_guesses} remaining guesses left')

    if remaining_guesses <= 0:
        gameOver = True
        print(f'\n\n{film}\n\n')
        break
    string = ''
    for i in obfuscated_array:
        string += i
    print(string)
