import time
from j2l.pytactx.agent import Agent
from cfg import *
from math import sin, cos, pi

referee = Agent(
    playerId=playerId,
    arena=arena,
    username=username,
    password=password,
    server=server,
    verbosity=verbosity
)

agentsStreaks = {}


def updateAgentPosition():
    """
    Update player positions and place a wall behind them
    """
    global agentsStreaks

    fsMap = referee.map

    for agentName, agentAttributes in referee.range.items():
        agentDir = agentAttributes["dir"]
        agentX = agentAttributes["x"]
        agentY = agentAttributes["y"]

        nextX = agentX + int(cos(agentDir * (pi / 2)))
        nextY = agentY + int(sin(agentDir * (pi / 2)))

        agentsStreaks[agentName].append((nextX, nextY))
        fsMap[agentY][agentX] = 2

        referee.rulePlayer(agentName, "x", nextX)
        referee.rulePlayer(agentName, "y", nextY)
        referee.ruleArena("map", fsMap)


def main():
    while True:
        updateAgentPosition()
        time.sleep(0.3)
        referee.update()


main()
