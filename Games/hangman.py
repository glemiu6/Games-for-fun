import random
def hangman():
    print("Welcome to Hangman!")
    print("You have 7 incorrect guesses to get out of the game.")
    print("Good luck!")
    with open('words.txt','r') as f:
        cuvinte=f.read().splitlines()
    word=random.choice(cuvinte)
    progress=['_']*len(word)
    print(f"The word is: {' '.join(progress)}")
    used_letters = set()
    guesses = 7
    while guesses > 0:
        guess = input("Guess a letter: ").lower()
        if guess in used_letters:
            print(f"You already guessed the letter '{guess}'. Try a different one!")
            continue
        used_letters.add(guess)
        if guess in word:
            print(f"You guessed the letter: {guess}")

            for index, letter in enumerate(word):
                if letter == guess:
                    progress[index] = guess


            print(''.join(progress))


            if ''.join(progress) == word:
                print("Congrats , you won!")
                break

        else:
            print('Sorry, wrong letter :(')
            guesses -= 1
            print(f'Now you have {guesses} guesses left')
            print(f"The word was: {' '.join(progress)}")


    if guesses == 0:
        print(f"You lost! The word was: {word}")




hangman()