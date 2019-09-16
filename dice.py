
from random import choices
ntrials = 10000
player1_wins = 0
n_player1dice = 3
n_player2dice = 2
player1_sum = 0
player2_sum = 0
for i in range(ntrials):
    # Player 2
    dice2 = choices(range(1,7),k = n_player2dice)
    if dice2[0] == dice2[1]:
        continue
    player2_sum = player2_sum + dice2[0] + dice2[1]
    # Player 1
    dice1 = choices(range(1,7),k = n_player1dice)
    dice1.sort(reverse = True)
    player1_sum = player1_sum + dice1[0] + dice1[1]

    if player1_sum > player2_sum:
        player1_wins = player1_wins + 1

    
print("Average player1wins =%5.2f" %(player1_wins/ntrials))
