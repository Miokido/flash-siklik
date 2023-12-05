from j2l.pytactx.agent import Agent
from main import fsMap
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

    def useItem(self, agent, item: str) -> None:
        if item in agent.getItems():
            agent.getItems().remove(item)

    def spawnItem(self) -> None:
        x = randint(0, 49)
        y = randint(0, 49)
        if fsMap[x][y] == 0:
            fsMap[x][y] = 3
        else:
            self.spawnItem()
