from j2l.pytactx.agent import Agent
from ..api.fs.Vehicle import Vehicle
from random import *


class IItemArbiter:
    def spawnItem(self, game_map: [[], []]) -> None:
        """
        Add an item on the map
        """
        ...

    def retrieveItem(self, agent: Agent, item: str, game_map: [[], []]) -> None:
        """
        Add the item to the list of the agent
        """
        ...


class ItemArbiter(IItemArbiter):
    def __init__(self, agent: Agent) -> None:
        self.__pytactxAgent = agent

    def spawnItem(self, game_map: [[], []]) -> None:
        x = randint(0, 50)
        y = randint(0, 50)
        if game_map[x][y] == 0:
           game_map[x][y] = 3
        else: self.spawnItem(game_map)

    def retrieveItem(self, agent: Agent, item: str, game_map: [[], []]) -> None:
        x = agent.getX()
        y = agent.getY()
        if game_map[x][y] == 3:
            game_map[x][y] = 0
            agent.addItem(item)
