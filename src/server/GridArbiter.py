import copy
import cfg
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

    def getRange(self):
        return self.__agent.range

    def updateAndPull(self):
        self.__agent.update(False)
        time.sleep(3)
        self.__agent.update(False)

    def clearPlayers(self):
        print("Resetting players...")

        for playerName, playerAttributes in self.__agent.range.items():
            self.rulePlayer(playerName, "life", 0)
            self.ruleArena('delPlayer', [playerName])

        self.ruleArena("reset", True)
        self.updateAndPull()

    def clearMap(self):
        print("Cleaning map...")
        map = copy.deepcopy(self.__agent.map)

        for i in range(len(map)):
            for j in range(len(map[i])):
                map[i][j] = 0

        self.ruleArena("map", map)

        self.updateAndPull()

    def setMap(self):
        print("Setting map parameters...")

        self.ruleArena(
            "bgImg",
            "https://raw.githubusercontent.com/Miokido/flash-siklik/main/res/background_grid.png"
        )
        self.ruleArena("gridColumns", 50)
        self.ruleArena("gridRows", 50)
        self.ruleArena("mapFriction", 0)
        self.ruleArena("maxPlayers", 5)

        self.updateAndPull()

    def createPlayers(self):
        """
        For all players in the rules, create the agent
        """
        print("Creating players...")

        for player, playerAttributes in playerRulesDict["players"].items():
            for attributeKey, attributeValue in playerAttributes.items():
                self.rulePlayer(player, attributeKey, attributeValue)

        self.updateAndPull()

    def initGrid(self):
        global playerRulesDict

        with open(os.path.join(__fileDir__, 'serverRules.json')) as json_data:
            playerRulesDict = json.load(json_data)

        self.clearPlayers()
        self.clearMap()
        self.setMap()
        self.createPlayers()

        cfg.globalMap = self.__agent.map
        cfg.globalPlayers = self.getRange()
