import random

choices = ['rock', 'paper', 'scissors']   

def checkChoice(c):
    computerChoice = random.choice(choices)
    winningPairs = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    if c == computerChoice:
        return ['tied', computerChoice]
    else:
        for i in winningPairs:
            if c == i and computerChoice == winningPairs[i]:
                return ['win', computerChoice]
        return ['lose', computerChoice]
    
def playAgain():
    y = input('Do you want to play again?\n')
    playGame() if y.lower().startswith('y') else exit()

def playGame():
    x = input('Rock, paper, or scissors?\n')
    x = x.strip().lower()

    if x not in choices:
        playGame()
    else:
        returnedArr = checkChoice(x)

        if returnedArr[0] == 'win':
            print(f'You Win! computer chose {returnedArr[1]}')
        elif returnedArr[0] == 'lose':
            print(f'You Lose! computer chose {returnedArr[1]}')
        else:
            print(f'You Tied! computer chose {returnedArr[1]}')

        playAgain()
                 
if __name__ == '__main__':

    s = input('Do you want to play a game?\n')
    if s.lower().startswith('y'):
        playGame()
