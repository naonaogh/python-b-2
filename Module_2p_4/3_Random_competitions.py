import random

team1 = [round(random.uniform(5, 10), 2) for i in range(21)]
team2 = [round(random.uniform(5, 10), 2) for j in range(21)]
win = [(max(team1[x], team2[x])) for x in range(21)]
print('\n',team1, '\n',team2, '\n',win)