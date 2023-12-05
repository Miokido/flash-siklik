import time

from DeathArbiter import DeathArbiter
from PlayerMovesArbiter import PlayerMovesReferee
from GridArbiter import GridArbiter, initServerRules
from TimerReferee import TimerReferee
from cfg import *

initServerRules()

gridReferee = GridArbiter(gridRefereeAgent)
deathReferee = DeathArbiter(deathRefereeAgent)
playerMovesReferee = PlayerMovesReferee(playerMovesRefereeAgent)
timerReferee = TimerReferee(timerRefereeAgent)


def getAlivePlayers():
    for playerName, playerAttributes in gridRefereeAgent.players:
        ...


def main():
    gridReferee.update()
    while True:
        time.sleep(0.3)
        playerMovesReferee.update()
        deathReferee.update()


main()
