import j2l.pytactx.agent as pytactx
import os
import json
import time

__fileDir__ = "./"
playerRulesDict = dict()


def initServerRules():
    global playerRulesDict
    with open(os.path.join(__fileDir__, 'serverRules.json')) as json_data:
        playerRulesDict = json.load(json_data)


class GridArbiter:
    def __init__(self, agent):
        self.__agent = agent
        self.__agent.rulePlayer(agentId=agent.robotId, attributeName="invisible", attributeValue=True)
        self.__agent.rulePlayer(agentId=agent.robotId, attributeName="invincible", attributeValue=True)

    def ruleArena(self, key, value):
        self.__agent.ruleArena(key, value)

    def createPlayers(self):
        for player, playerAttributes in playerRulesDict["players"].items():
            for attributeKey, attributeValue in playerAttributes.items():
                self.__agent.rulePlayer(player, attributeKey, attributeValue)

    def update(self):
        self.initGrid()

    def getRange(self):
        return self.__agent.range

    def clearPlayers(self):
        self.__agent.ruleArena("reset", True)

    def clearPlayer(self, name):
        for player, playerAttributes in self.__agent.range.items():
            self.__agent.rulePlayer(player, 'life', 0)
            self.__agent.ruleArena('delPlayer', [player])

    def clearMap(self):
        for i in range(len(self.__agent.map)):
            for j in range(len(self.__agent.map[i])):
                self.__agent.map[i][j] = 0

    def initGrid(self):
        self.clearPlayers()
        self.clearMap()
        self.__agent.update()
        time.sleep(0.3)
        self.ruleArena(
            "bgImg",
            "https://raw.githubusercontent.com/Miokido/flash-siklik/main/res/background_grid.png"
        )
        self.ruleArena("gridColumns", 50)
        self.ruleArena("gridRows", 50)
        self.ruleArena("mapFriction", 0)
        self.createPlayers()
        self.__agent.update()
