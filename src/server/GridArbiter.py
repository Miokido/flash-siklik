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

    def ruleArena(self, key, value):
        self.__agent.ruleArena(attributeName=key, attributeValue=value)

    def rulePlayer(self, agentId, key, value):
        self.__agent.rulePlayer(agentId=agentId, attributeName=key, attributeValue=value)

    def getRange(self):
        return self.__agent.range

    def updateAndPull(self):
        """
        Updates the game, waits 3 seconds and pull data from server
        """
        self.__agent.update(False)
        time.sleep(3)
        self.__agent.update(False)

    def clearPlayers(self):
        """
        Kill and delete all players
        """
        print("Resetting players...")

        for playerName, playerAttributes in self.__agent.range.items():
            self.rulePlayer(playerName, "life", 0)
            self.ruleArena('delPlayer', [playerName])

        self.ruleArena("reset", True)
        self.updateAndPull()

    def cleanMap(self):
        """
        Reset all map cells
        """
        print("Cleaning map...")
        map = copy.deepcopy(self.__agent.map)

        for i in range(len(map)):
            for j in range(len(map[i])):
                map[i][j] = 0

        self.ruleArena("map", map)
        self.ruleArena("players", [])

        self.updateAndPull()

    def setMap(self):
        """
        Sets the map settings
        """
        print("Setting map parameters...")

        for ruleName, ruleAttribute in playerRulesDict["arena"].items():
            self.ruleArena(ruleName, ruleAttribute)

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

        with open(os.path.join(__fileDir__, 'gameRules.json')) as json_data:
            playerRulesDict = json.load(json_data)

        self.clearPlayers()
        self.cleanMap()
        self.setMap()
        self.createPlayers()

        cfg.globalMap = self.__agent.map
        cfg.globalPlayers = self.__agent.range
