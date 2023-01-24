import random

print('Hello. What is your name?')
name = input()
print('Well ' + str(name) + ' I am thinking of a number between 1 and 20.')
number = random.randint(1, 20)
for guessesTaken in range(1, 5):
    print('Take a guess.')
    guess = int(input())
    if guess > number:
        print('Your guess is too high.')
    elif guess < number:
        print('Your guess is too low.')
    else:
        break
if guess == number:
    print('Good job! You guessed the correct number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope! You took ' + str(guessesTaken) + ' guesses. The correct number was ' + str(number) + '.')
