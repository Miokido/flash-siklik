import j2l.pytactx.agent as pytactx
import os
import json

__fileDir__ = "./"
playerRulesdict = dict()

with open(os.path.join(__fileDir__, 'PlayerRules.json')) as json_data:
  playerRulesdict = json.load(json_data)


class MainArbiter:

  def __init__(self):
    self.__agent = pytactx.Agent(playerId=input("playerId"),
                                 arena="flashsiklik",
                                 username="demo",
                                 password="demo",
                                 server="mqtt.jusdeliens.com",
                                 verbosity=2)

  def ruleArena(self, key, value):
    self.__agent.ruleArena(key, value)

  def createPlayers(self):
    for player, playerAttributes in playerRulesdict["players"].items():
      for attributeKey, attributeValue in playerAttributes.items():
        self._MainArbiter__agent.rulePlayer(player, attributeKey,
                                            attributeValue)

  def update(self):
    self.__agent.update()

  def getRange(self):
    return self.__agent.range()

  def clearPlayers(self):
    ...


def initGrid():
  mainArbiter.clearPlayers()
  mainArbiter.ruleArena("bgImg", "https://github.com/Miokido/flash-siklik/blob/4e36fc4a47e6788a63bd5436d6c550e0ee5d2dec/res/background_grid.png")
  mainArbiter.ruleArena("gridColumns", 50)
  mainArbiter.ruleArena("gridRows", 50)
  mainArbiter.ruleArena("mapFriction", 0)
  mainArbiter.createPlayers()


mainArbiter = MainArbiter()
initGrid()
mainArbiter.update()
