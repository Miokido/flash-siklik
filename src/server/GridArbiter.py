import j2l.pytactx.agent as pytactx


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

  def createPlayers(self, rulesFile):
    self.printInfoToArena("⌛ Création des joueurs ...")
    for player, playerAttributes in rulesFile["playersRules"].items():
      for attributeKey, attributeValue in playerAttributes.items():
        self.__pytactxAgent.rulePlayer(player, attributeKey, attributeValue)


def initGrid():
  mainArbiter = MainArbiter()
  mainArbiter.ruleArena("bgImg", "/path/")
  mainArbiter.ruleArena("gridColumns", 50)
  mainArbiter.ruleArena("gridRows", 50)
  mainArbiter.ruleArena("mapFriction", 0)
  #mainArbiter.ruleArena("bgImg", "")

  coords = [[13, 10], [26, 10], [39, 10], [13, 20], [39, 20], [13, 30],
            [39, 30], [13, 40], [26, 40], [39, 40]]
  for coord in coords:
    ...
    #self.__agent.pose(x, y, orientation)
  #positionner joueur
  #appeler ObjectArbiter
  #appeler TimerArbiter
  #mainArbiter.


initGrid()
