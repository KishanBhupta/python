import keyword
import random

playerList = ("firstPlayer", "secondPlayer", "thirdPlayer", "fourthPlayer", "fifthPlayer", "sixPlayer")
totOver = int(input("Enter total over"))
totBall = totOver * 6
totFilter = (1, 2, 4, 6, "BW", "RO", "CO")
wicketCount = 0
player = 0

for ball in range(totBall):
    if (ball % 2 == 0):
        for player in playerList:
            input(player + "Are you Ready ?? ")
            if (keyword.__all__):
                randIteam = random.choice(totFilter)
                print(randIteam)
            if (randIteam == "BW" or randIteam == "CO" or randIteam == "RO"):
                player = playerList.index(next(1))
        else:
            for player in playerList:
                input(player + "Are you Ready ?? ")
                if (keyword.__all__):
                    randIteam = random.choice(totFilter)
                    print(randIteam)
                if (randIteam == "BW" or randIteam == "CO" or randIteam == "RO"):
                    player = playerList.index(next(1))
