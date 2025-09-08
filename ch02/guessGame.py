import random

print("Welcome to the Guessing Game!")
print("Take a guess between 1 and 20.")


randomNumber = random.randint(1, 20)

howManyTry = 0

while True:
    howManyTry += 1
    userGuess = int(input("your guess: "))
    if userGuess == randomNumber:
        print('good job! you guessed my number in {} guesses!'.format(howManyTry))
        break
    if userGuess >= randomNumber:
        print('your guess is too high')
    if userGuess <= randomNumber:
        print('your guess is too low')

