from j2l.pytactx.agent import Agent
from random import randint
from cfg import globalMap



class IItemArbiter:
    def retrieveItem(self, agent, item: str) -> None:
        """
        Add the item to the list of the agent
        """
        ...

    def useItem(self, agent, item: str) -> None:
        """
        Use and remove the item from the agent list
        """
        ...

    def spawnItem(self) -> None:
        """
        Spawn an item at regular interval
        """
        ...


class ItemArbiter(IItemArbiter):
    def __init__(self, agent: Agent) -> None:
        self.__agent = agent
        self.__agent.rulePlayer(agentId=agent.robotId, attributeName="invisible", attributeValue=True)
        self.__agent.rulePlayer(agentId=agent.robotId, attributeName="invincible", attributeValue=True)


    def spawnItem(self) -> None:
        """
        Spawn an item at regular interval if less than 3 on map
        """
        x = randint(0, 49)
        y = randint(0, 49)
        if globalMap[y][x] == 0:
            globalMap[y][x] = 3
        else:
            self.spawnItem()

    def update(self, enableSleep=True):
        for player in self.__agent.game.players:
            if globalMap[player.x][player.y] == 3:
                item = randint(0, 3)
                if item == 0:
                    player.addItem('boost')
                if item == 1:
                    player.addItem('superBoost')
                if item == 2:
                    player.addItem('ghost')
                if item == 3:
                    player.addItem('shield')
                self.__agent.update(enableSleep)
