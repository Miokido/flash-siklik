import copy

import cfg
import time
from cfg import *

from GridArbiter import GridArbiter
from DeathArbiter import DeathArbiter
from PlayerMovesArbiter import PlayerMovesReferee
from ItemArbiter import ItemArbiter

gridReferee = GridArbiter(agent)
deathReferee = DeathArbiter(agent)
playerMovesReferee = PlayerMovesReferee(agent)
itemReferee = ItemArbiter(agent)
def main():
    global gridReferee

    i = 0

    gridReferee.initGrid()

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

        if i < 10:
            gridReferee.ruleArena("map", cfg.globalMap)
            i = 0
        elif i == 10:
            cfg.globalMap = copy.deepcopy(agent.map)
            cfg.globalPlayers = copy.deepcopy(agent.range)

        i = i + 1

        agent.update()
        time.sleep(0.333)


main()
