from cfg import globalMap


class IDeathArbiter:
    def killVehicle(self, agent):
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
        # self.__agent.ruleArena('delPlayer', [agentName])

    def checkForAgentDeletion(self):
        for agentName, agentAttributes in items():
            agentX = agentAttributes["x"]
            agentY = agentAttributes["y"]

            case = globalMap[agentY][agentX]

            if case == 2:
                self.killVehicle(agentName)

    def update(self, enableSleep=True):
        self.checkForAgentDeletion()
        self.__agent.update(enableSleep)
