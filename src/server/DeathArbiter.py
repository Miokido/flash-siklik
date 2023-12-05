from j2l.pytactx.agent import Agent
from main import fsMap


class IDeathArbiter:
    def killVehicle(self, vehicle):
        """
            this method kills the vehicle
            :param vehicle: Vehicle
            :return: void
        """
        pass

    def update(self):
        pass


class DeathArbiter(IDeathArbiter):
    def __init__(self, agent):
        self.__agent = agent

    def killVehicle(self, agentName):
        """
            this method kills the vehicle
            :param agentName:
            :return: void
        """
        self.__agent.rulePlayer(agentName, 'life', 0)
        self.__agent.ruleArena('delPlayer', [agentName])

    def checkForAgentDeletion(self):
        for agentName, agentAttributes in self.__agent.range.items():
            agentX = agentAttributes["x"]
            agentY = agentAttributes["y"]

            if fsMap[agentY][agentX] > 0:
                self.killVehicle(agentName)

    def update(self):
        self.checkForAgentDeletion()
        self.__agent.update()
