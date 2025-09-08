import random

print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0

while True:
    print("{} Wins, {} Losses, {} Ties".format(wins, losses, ties))
    userChoice = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ')
    computerChoice = random.randint(1,3)


    if userChoice == 'r':
        print('ROCK versus...')
    elif userChoice == 'p':
        print('PAPER versus...')
    elif userChoice == 's':
        print('SCISSORS versus...')
    else:
        break

    if computerChoice == 1:
        computerChoice = 'p'
        print('PAPER')
    elif computerChoice == 2:
        computerChoice = 'r'
        print('ROCK')
    elif computerChoice == 3:
        computerChoice = 's'
        print('SCISSORS')
    else:
        break

    if userChoice == computerChoice:
        print('It\'s a tie')
        ties += 1
    if userChoice == 'r' and computerChoice == 'p':
        print('you lose')
        losses += 1
    if userChoice == 'r' and computerChoice == 's':
        wins += 1
        print('you win')
    if userChoice == 'p' and computerChoice == 'r':
        wins += 1
        print('you win')
    if userChoice == 'p' and computerChoice == 's':
        losses += 1
        print('you lose')
    if userChoice == 's' and computerChoice == 'p':
        wins += 1
        print('you win')
    if userChoice == 's' and computerChoice == 'r':
        losses += 1
        print('you lose')           
                 