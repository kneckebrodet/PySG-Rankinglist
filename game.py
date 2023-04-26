from psg import RankingWindow, NewGameWindow
from random import randint

rankings = [
    ["Lucas", 87],
    ["Sara", 48],
    ["Tanaka", 63],
    ["Ami", 92],
]

while True:
    newgame = NewGameWindow()
    new_player = [newgame.run(), randint(1,100)]
    rankings.append(new_player)
    rank = RankingWindow(rankings)
    rank.run()