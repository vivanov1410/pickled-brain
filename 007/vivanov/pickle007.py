from random import randint


words = ['popas', 'sveta', 'slava', 'lublu']
word = words[randint(0, len(words) - 1)]

print('I chose a word, try to guess it...')

while True:
    result = ''
    guess = raw_input('Your guess: ')

    if guess == word:
        break

    for i in range(len(guess)):
        letter_in_guess = guess[i]
        got_it = False
        for k in range(len(word)):
            letter_in_word = word[k]
            if letter_in_guess == letter_in_word:
                got_it = True
                if i == k:
                    result += '[' + letter_in_guess + ']'
                    break
                else:
                    result += '(' + letter_in_guess + ')'
                    break
        if not got_it:
            result += letter_in_guess

    print('Clue: {0}'.format(result))

print('You won')
exit()