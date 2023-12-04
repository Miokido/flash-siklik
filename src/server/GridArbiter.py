import j2l.pytactx.agent as pytactx
import os
import json
import time

__fileDir__ = "./"
playerRulesdict = dict()

with open(os.path.join(__fileDir__, 'PlayerRules.json')) as json_data:
  playerRulesdict = json.load(json_data)


class GridArbiter:

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
        self.__agent.rulePlayer(player, attributeKey, attributeValue)

  def update(self):
    self.__agent.update()

  def getRange(self):
    return self.__agent.range

  def clearPlayers(self):
    self.__agent.ruleArena("reset", True)

  def clearPlayer(self, name):
    for player, playerAttributes in self.__agent.range.items():
      self.__agent.rulePlayer(player, 'life', 0)
      self.__agent.ruleArena('delPlayer', [player])


def initGrid():
  gridArbiter.clearPlayers()
  gridArbiter.update()
  time.sleep(0.3)
  gridArbiter.ruleArena(
    "bgImg",
    "https://raw.githubusercontent.com/Miokido/flash-siklik/main/res/background_grid.png"
  )
  gridArbiter.ruleArena("gridColumns", 50)
  gridArbiter.ruleArena("gridRows", 50)
  gridArbiter.ruleArena("mapFriction", 0)
  gridArbiter.createPlayers()


gridArbiter = GridArbiter()
initGrid()
gridArbiter.update()
