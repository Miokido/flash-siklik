from j2l.pytactx.agent import Agent
from cfg import *
from math import sin, cos, pi


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
        fsMap = self.__agent.map

        for agentName, agentAttributes in self.__agent.range.items():
            agentDir = agentAttributes["dir"]
            agentX = agentAttributes["x"]
            agentY = agentAttributes["y"]

            nextX = agentX + int(cos(agentDir * (pi / 2)))
            nextY = agentY + int(sin(agentDir * (pi / 2)))

            self.__agentsStreaks[agentName].append((nextX, nextY))
            fsMap[agentY][agentX] = 2

            self.__agent.rulePlayer(agentName, "x", nextX)
            self.__agent.rulePlayer(agentName, "y", nextY)
            self.__agent.ruleArena("map", fsMap)

    def update(self):
        self.update()
