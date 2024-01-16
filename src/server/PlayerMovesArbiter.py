from math import sin, cos, pi

import cfg

class IPlayerMovesReferee:
    def updateAgentPosition(self):
        ...


class PlayerMovesReferee(IPlayerMovesReferee):
    def __init__(self, agent):
        self.__agent = agent
        self.__agentsStreaks = {}

    def updateAgentPosition(self):
        """
        Update player positions and place a wall behind them
        """
        for agentName, agentAttributes in cfg.globalPlayers.items():
            if agentAttributes["life"] > 0:
                agentDir = agentAttributes["dir"]
                agentX = agentAttributes["x"]
                agentY = agentAttributes["y"]

                nextX = agentX + int(cos(agentDir * (pi / 2)))
                nextY = agentY - int(sin(agentDir * (pi / 2)))

                if 0 <= nextX <= 49 and 0 <= nextY <= 49:
                    self.__agent.rulePlayer(agentName, "x", nextX)
                    self.__agent.rulePlayer(agentName, "y", nextY)
                    cfg.globalMap[agentY][agentX] = 2

    def update(self, enableSleep=True):
        self.updateAgentPosition()
        #self.__agent.update(enableSleep)
