from math import sin, cos, pi


class IPlayerMovesReferee:
    def updateAgentPosition(self):
        ...


class PlayerMovesReferee(IPlayerMovesReferee):
    def __init__(self, agent):
        self.__fsMap = None
        self.__fsPlayers = None
        self.__agent = agent
        self.__agentsStreaks = {}

    def updateAgentPosition(self):
        """
        Update player positions and place a wall behind them
        """
        for agentName, agentAttributes in self.__fsPlayers.items():
            if agentAttributes["life"] > 0:
                agentDir = agentAttributes["dir"]
                agentX = agentAttributes["x"]
                agentY = agentAttributes["y"]

                nextX = agentX + int(cos(agentDir * (pi / 2)))
                nextY = agentY - int(sin(agentDir * (pi / 2)))

                if 0 <= nextX <= 49 and 0 <= nextY <= 49:
                    self.__fsPlayers[agentName]["x"] = nextX
                    self.__fsPlayers[agentName]["y"] = nextY
                    self.__fsMap[agentY][agentX] = 2

    def setGameData(self, fsMap, fsPlayers):
        self.__fsMap = fsMap
        self.__fsPlayers = fsPlayers

    def update(self):
        if not self.__fsMap or self.__fsPlayers is None:
            return

        self.updateAgentPosition()
        self.__agent.update()
