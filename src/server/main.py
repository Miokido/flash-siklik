import time

from DeathArbiter import DeathArbiter
from PlayerMovesArbiter import PlayerMovesReferee
from GridArbiter import GridArbiter
from TimerReferee import TimerReferee
from cfg import *

gridReferee = GridArbiter(gridRefereeAgent)
deathReferee = DeathArbiter(deathRefereeAgent)
playerMovesReferee = PlayerMovesReferee(playerMovesRefereeAgent)
timerReferee = TimerReferee(timerRefereeAgent)


def getAlivePlayers():
    for playerName, playerAttributes in gridRefereeAgent.players:
        ...


gridReferee.initGrid()
fsMap = gridReferee.getMap()


def main():
    gridReferee.update()
    time.sleep(3)

    i = 0

    while True:
        time.sleep(0.3)
        playerMovesReferee.update()
        deathReferee.update()

        if i == 4:
            gridReferee.ruleArena("map", fsMap)
            i = 0
        else:
            i = i + 1


main()
