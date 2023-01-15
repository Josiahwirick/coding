### Basic slot machine game
### Enter a bet, checks for any matching combination horizontally and diagonally
### Not balanced because I don't know how to rig gambling
### - Josiah Wirick

import random

# Initialize player's starting amount and winning payouts
money = 100
payouts = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print('Your starting balance is: 100$')

# The machine
while True:
    # Ask player to make a bet
    bet = input("Enter your bet (q to quit): ")
    if bet == 'q':
        break
    if bet.isdigit(): # Validate if a positive number is entered
        bet = int(bet)
    else:
        print('Must be a number that is not negative.')
        continue

    
    # Check if player has enough money to make the bet
    if bet > money:
        print("You don't have enough money to make that bet.")
        continue
    
    # Spin the reels
    """ Commented out the eyesore of a complicated setup to generate the grid for something more elegant
    grid1 = random.choice(list('AAAAABBBBCCCDDE'))
    grid2 = random.choice(list('AAAAABBBBCCCDDE'))
    grid3 = random.choice(list('AAAAABBBBCCCDDE'))
    grid4 = random.choice(list('AAAAABBBBCCCDDE'))
    grid5 = random.choice(list('AAAAABBBBCCCDDE'))
    grid6 = random.choice(list('AAAAABBBBCCCDDE'))
    grid7 = random.choice(list('AAAAABBBBCCCDDE'))
    grid8 = random.choice(list('AAAAABBBBCCCDDE'))
    grid9 = random.choice(list('AAAAABBBBCCCDDE'))"""
    
    grid = [[random.choice(list('AAAAABBBBCCCDDE')) for _ in range(3)] for _ in range(3)]
    print("Spinning reels...")
    print(grid[0])
    print(grid[1])
    print(grid[2])
    
    # Check for a winning combination
    win = False
    for i in range(3):
        if (grid[i][0] == grid[i][1] == grid[i][2]) or (grid[0][i] == grid[1][i] == grid[2][i]):
            win = True
            winning_letter = grid[i][0]
            break
    if grid[0][0] == grid[1][1] == grid[2][2] or grid[2][0] == grid[1][1] == grid[0][2]:
        win = True
        winning_letter = grid[1][1]
    if win:
        payout = payouts[winning_letter] * bet
        money += payout
        print(f"You won ${payout}! Your new balance is ${money}.")
    else:
        money -= bet
        print(f"You lost ${bet}. Your new balance is ${money}.")
    
    # Check if player has run out of money
    if money <= 0:
        print("You have run out of money. Game over.")
        break
