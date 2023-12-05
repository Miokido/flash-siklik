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
        self.__fsMap = None
        self.__fsPlayers = None

    def killVehicle(self, agentName):
        """
            this method kills the vehicle
            :param agentName:
            :return: void
        """
        self.__agent.rulePlayer(agentName, 'life', 0)
        self.__agent.ruleArena('delPlayer', [agentName])

    def checkForAgentDeletion(self):
        for agentName, agentAttributes in self.__fsPlayers.items():
            agentX = agentAttributes["x"]
            agentY = agentAttributes["y"]

            case = self.__fsMap[agentY][agentX]

            print(agentName + " : " + str(case))

            if case == 2:
                self.killVehicle(agentName)

    def setGameData(self, fsMap, fsPlayers):
        self.__fsMap = fsMap
        self.__fsPlayers = fsPlayers

    def update(self):
        if self.__fsMap is None:
            return

        self.checkForAgentDeletion()
        self.__agent.update()
