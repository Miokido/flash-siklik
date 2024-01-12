import copy

from cfg import globalMap


import os
import json
import time

__fileDir__ = "./"
playerRulesDict = dict()

class GridArbiter:
    def __init__(self, agent):
        self.__agent = agent
        self.__agent.rulePlayer(agentId=agent.robotId, attributeName="invisible", attributeValue=True)
        self.__agent.rulePlayer(agentId=agent.robotId, attributeName="invincible", attributeValue=True)

    def ruleArena(self, key, value):
        self.__agent.ruleArena(attributeName=key, attributeValue=value)

    def rulePlayer(self, agentId, key, value):
        self.__agent.rulePlayer(agentId=agentId, attributeName=key, attributeValue=value)

    def createPlayers(self):
        for player, playerAttributes in playerRulesDict["players"].items():
            for attributeKey, attributeValue in playerAttributes.items():
                self.rulePlayer(player, attributeKey, attributeValue)

        print("createPlayers")
        self.__agent.update(False)
        time.sleep(3)

    def getRange(self):
        return self.__agent.range

    def clearPlayers(self):
        self.ruleArena("reset", True)
        self.__agent.update(False)
        print("Reseting players...")
        time.sleep(3)

    def clearMap(self):
        map = copy.deepcopy(self.__agent.map)

        for i in range(len(map)):
            for j in range(len(map[i])):
                map[i][j] = 0

        self.ruleArena("map", map)

        self.__agent.update(False)
        print("Cleaning map...")
        time.sleep(3)

    def initGrid(self):
        global playerRulesDict

        with open(os.path.join(__fileDir__, 'serverRules.json')) as json_data:
            playerRulesDict = json.load(json_data)

        self.clearPlayers()
        self.clearMap()

        self.ruleArena(
            "bgImg",
            "https://raw.githubusercontent.com/Miokido/flash-siklik/main/res/background_grid.png"
        )
        self.ruleArena("gridColumns", 50)
        self.ruleArena("gridRows", 50)
        self.ruleArena("mapFriction", 0)
        self.ruleArena("maxPlayers", 4)

        self.__agent.update(False)
        print("Setting map parameters...")
        time.sleep(3)
        self.__agent.update(False)

        self.createPlayers()

        self.__agent.update(False)
        print("Creating players...")
        time.sleep(3)
        self.__agent.update(False)
