secretWord = "Kebab"
letterGuessed = ""

failureCount = 6

while failureCount > 0:
    guess = input(" Enter a letter: ")
    if guess in secretWord:
        print(f'Correct! There is one or more {guess} in the secre word.')
    else:
        failureCount -= 1
        print(f'Incorrect. There ar e no {guess} in the secret word. {failureCount} turns left.')

    letterGuessed = letterGuessed + guess
    wrongLetterCount = 0

    for letter in secretWord:
        if letter in letterGuessed:
            print(f'{letter}', end="")
        else:
            print("_", end="")
            wrongLetterCount += 1

    if wrongLetterCount == 0:
        print(f'Congrts! The secret word was: {secretWord}. You won!')
        break
else:
    print("Sorry, you didnt win it this time. try again!")
