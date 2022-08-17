# Coin Flip
import random
numberOfStreaks = 0
streak = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    list = []
    for i in range(100):
        if random.randint(0,1) == 0:
            list.append('H')
        else:
            list.append('T')
        
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(list)):
        if list[i] == 0:
            pass
        elif list[i] == list[i - 1]:
            streak += 1
        else:
            streak = 0
            
        if streak == 6:
            numberOfStreaks += 1
            
    list = []
print('Chance of streak: %s%%' % (numberOfStreaks / 100))