"""
File: hangman_extension.py
Name: Chiachien Li 李佳謙
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random


def main():
    """
    People can play hangman game with this program.
    It will randomly import words. People can guess the characters in the word.
    The numbers people can guess is controlled by N_TURNS.
    Once people guess a wrong character, they will lose one chance to guess.
    If it's correct, they will not lose chance.
    If the format input is not one single character, it will print "illegal format".
    People will win if the answer is completely spelled before the chances used up.
    People will lose if the answer is not completely spelled when the chances used up.
    """
    answer = random_word()
    # Case-insensitive.
    answer = answer.upper()
    # "Blank" will be the word looks like.
    blank = ''
    # Show the number of the characters first.
    for i in range(len(answer)):
        blank += '-'
    print('The word looks like: ' + blank)
    # The remaining chances to guess
    print('You have 7 guesses left.')
    # Picture before guess.
    zero()
    guess_word(answer, blank)
    # Show the answer
    print('The word was: ' + answer)


def guess_word(answer, blank):
    """
    This function will recognize the format of the character guessed. If the alphabet guessed is in the word, it will
    will show as a hint. If it's not, chance will lose.
    -------------------------------------------------
    :param answer: The answer word.
    :param blank: The empty string not guessed yet.
    """
    # x is the times guessed wrong.
    x = 0
    while True:
        # Ask for new guess in every round.
        guess = input('Your guess: ')
        # Check if it's a alphabet
        if guess.isalpha():
            # If the input is not one character, it's an illegal format.
            if len(guess) != 1:
                print('illegal format.')
            else:
                # Case-insensitive.
                guess = guess.upper()
                # There is at least one correct character in the word.
                if guess in answer:
                    # Find the position of the correct character.
                    for k in range(len(answer)):
                        if guess == answer[k]:
                            # Restructure the "blank" and show the correct character.
                            pre_answer = blank[:k]
                            pre_answer += guess
                            pre_answer += blank[k+1:]
                            blank = pre_answer
                    print('You are correct!')
                    # There are still more characters to find.
                    if '-' in blank:
                        print('The word looks like: ' + blank)
                        print('You have ' + str(7 - x) + ' guesses left.')
                        # Draw the according picture.
                        draw(x)

                    else:
                        print('You win!!')
                        # Winner's picture.
                        winner()
                        break
                else:
                    # If guessed wrong, x will plus one.
                    x += 1
                    # There still more chances to guess.
                    if x < 7:
                        print('There is no ' + guess + "'s in the word.")
                        print('The word looks like: ' + blank)
                        print('You have ' + str(7 - x) + ' guesses left.')
                        draw(x)
                    # The chances are used up.
                    else:
                        print('There is no ' + guess + "'s in the word.")
                        print('You are completely hung : (')
                        draw(x)
                        break
        # Input is not alphabet.
        else:
            print('illegal format.')


def draw(x):
    if x == 0:
        zero()
    elif x == 1:
        first()
    elif x == 2:
        second()
    elif x == 3:
        third()
    elif x == 4:
        forth()
    elif x == 5:
        fifth()
    elif x == 6:
        sixth()
    elif x == 7:
        seventh()


def zero():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    for j in range(3):
        print('   |')


def first():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    print('   |     O')
    for j in range(2):
        print('   |')


def second():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    print('   |     O')
    print('   |     |')
    for j in range(1):
        print('   |')


def third():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    print('   |     O')
    print('   |    /|')
    for j in range(1):
        print('   |')


def forth():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    print('   |     O')
    print('   |    /|\\')
    for j in range(1):
        print('   |')


def fifth():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    print('   |     O')
    print('   |    /|\\')
    print('   |    /')
    print('   |')


def sixth():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    print('   |     O')
    print('   |    /|\\')
    print('   |    / \\')
    print('   |')


def seventh():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    print('   |   (QAQ)')
    print('   |    /|\\')
    print('   |    / \\')
    print('   |    DEAD')


def winner():
    print('   ', end="")
    for i in range(6):
        print('-', end="")
    print('-')
    print('   |     |')
    print('   |  (*^ ^*)')
    print('   |    \\|/')
    print('   |    / \\')
    print('   |    WIN')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
