from j2l.pytactx.agent import Agent
from ..api.fs.Vehicle import Vehicle


class IItemArbiter:
    def retrieveItem(self, agent: Vehicle, item: str) -> None:
        """
        Add the item to the list of the agent
        """
        ...

    def useItem(self, agent: Vehicle, item: str) -> None:
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
        self.__pytactxAgent = agent

    def useItem(self, agent: Vehicle, item: str) -> None:
        if item in agent.getItems():
            agent.getItems().remove(item)

    def spawnItem(self) -> None:
        item = Agent()
