# this is a guess the number game
import random
print('hello. What is your name? ')
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20')

# ask the player to guess 6 times
for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # this condition is the correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number ' + str(guessTaken) + '  guesses.')
else:
    print('Nope. the num I was thining of was ' + str(secretNumber))

