import time
from cfg import *

from GridArbiter import GridArbiter
from DeathArbiter import DeathArbiter
from PlayerMovesArbiter import PlayerMovesReferee


def getGameInfos():
    return gridRefereeAgent.map, gridRefereeAgent.range


gridReferee = GridArbiter(gridRefereeAgent)
deathReferee = DeathArbiter(deathRefereeAgent)
playerMovesReferee = PlayerMovesReferee(playerMovesRefereeAgent)

(fsMap, fsPlayers) = gridReferee.initGrid()


def main():
    i = 0
    global fsMap, fsPlayers

    print(fsPlayers)

    print("C'est parti")

    while True:
        playerMovesReferee.update()
        deathReferee.update()

        if i % 2 == 0 and i != 10:
            gridReferee.ruleArena("map", fsMap)
            for agentName, agentAttributes in fsPlayers.items():
                gridRefereeAgent.rulePlayer(agentName, "x", agentAttributes["x"])
                gridRefereeAgent.rulePlayer(agentName, "y", agentAttributes["y"])
        elif i == 10:
            (fsMap, fsPlayers) = getGameInfos()
            gridReferee.setGameData(fsMap, fsPlayers)
            deathReferee.setGameData(fsMap, fsPlayers)
            playerMovesReferee.setGameData(fsMap, fsPlayers)
            i = 0

        i = i + 1

        gridRefereeAgent.update()


main()
