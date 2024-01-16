from cfg import *

from GridArbiter import GridArbiter
from DeathArbiter import DeathArbiter
from PlayerMovesArbiter import PlayerMovesReferee
from ItemArbiter import ItemArbiter


def getGameInfos():
    return gridRefereeAgent.map, gridRefereeAgent.range


gridReferee = GridArbiter(gridRefereeAgent)
deathReferee = DeathArbiter(deathRefereeAgent)
playerMovesReferee = PlayerMovesReferee(playerMovesRefereeAgent)
itemReferee = ItemArbiter(itemRefereeAgent)


def main():
    i = 0

    (fsMap, fsPlayers) = gridReferee.initGrid()

    print("C'est parti !")

    while True:
        nbItems = 0
        for line in fsMap:
            for tile in line:
                if tile == 3:
                    nbItems = nbItems + 1

        if nbItems < 5:
            itemReferee.spawnItem()
        playerMovesReferee.update()
        deathReferee.update()
        itemReferee.update()

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
