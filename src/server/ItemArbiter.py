from j2l.pytactx.agent import Agent
from random import randint


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
        self.__fsMap = None
        self.__fsPlayers = None

    def setGameData(self, fsMap, fsPlayers):
        self.__fsMap = fsMap
        self.__fsPlayers = fsPlayers

    def spawnItem(self) -> None:
        x = randint(0, 49)
        y = randint(0, 49)
        if self.__fsMap[x][y] == 0:
            self.__fsMap[x][y] = 3
        else:
            self.spawnItem()
