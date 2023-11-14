import j2l.pytactx.agent as pytactx


class ObjectArbiter:

  def __init__(self):
    self.agent = pytactx.Agent(playerId=input("playerId"),
                               arena="flashsiklik",
                               username="demo",
                               password="demo",
                               server="mqtt.jusdeliens.com",
                               verbosity=2)


def main():  #init grid
  objectArbiter = ObjectArbiter()
  objectArbiter.agent.ruleArena("gridColumns", 50)
  objectArbiter.agent.ruleArena("gridRows", 50)
  objectArbiter.agent.update()


main()
