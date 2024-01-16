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

        if True:
            gridReferee.ruleArena("map", cfg.globalMap)
            for agentName, agentAttributes in cfg.globalPlayers.items():
                agent.rulePlayer(agentName, "x", agentAttributes["x"])
                agent.rulePlayer(agentName, "y", agentAttributes["y"])
            i = 0
        elif 10:
            #cfg.globalMap = copy.deepcopy(agent.map)
            #cfg.globalMap = copy.deepcopy(agent.range)
            pass

        i = i + 1

        agent.update()
        time.sleep(0.333)


main()
