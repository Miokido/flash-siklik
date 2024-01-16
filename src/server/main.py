import copy

import cfg
from cfg import *

from GridArbiter import GridArbiter
from DeathArbiter import DeathArbiter
from PlayerMovesArbiter import PlayerMovesReferee
from ItemArbiter import ItemArbiter

gridReferee = GridArbiter(gridRefereeAgent)
deathReferee = DeathArbiter(gridRefereeAgent)
playerMovesReferee = PlayerMovesReferee(gridRefereeAgent)
itemReferee = ItemArbiter(gridRefereeAgent)


def main():
    global gridReferee

    i = 0

    gridReferee.initGrid()

    cfg.globalMap = gridRefereeAgent.map

    print("C'est parti !")

    while True:
        # nbItems = 0
        # for line in fsMap:
        #    for tile in line:
        #        if tile == 3:
        #            nbItems = nbItems + 1

        # if nbItems < 5:
        # itemReferee.spawnItem()
        playerMovesReferee.update(False)

        if True:
            gridReferee.ruleArena("map", cfg.globalMap)
            for agentName, agentAttributes in fsPlayers.items():
                gridRefereeAgent.rulePlayer(agentName, "x", agentAttributes["x"])
                gridRefereeAgent.rulePlayer(agentName, "y", agentAttributes["y"])
            i = 0
        elif 10:
            cfg.globalMap = copy.deepcopy(gridRefereeAgent.map)

        i = i + 1

        gridRefereeAgent.update()


main()
