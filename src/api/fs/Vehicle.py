import j2l.pytactx.agent as pytactx


class Vehicle:
    def __init__(self, playerId, arena, username, password, server, verbosity):
        self._agent = pytactx.Agent(playerId=playerId, arena=arena, username=username, password=password, server=server,
                                    verbosity=verbosity)
        self._items = None
        self._itemsUsed = None
        self._boost = False
        self._superBoost = False
        self._ghost = False
        self._shield = False

    def turn(self, direction):
        """
        Turn the player with the given direction
        """
        pass

    def boost(self, enable):
        """
        Enable or disable boost
        """
        pass

    def useItem(self, item):
        """
        Use the given item
        """
        pass

    def update(self):
        """
        Send update to the server
        """
        self._agent.update()
        pass

    def getItems(self):
        return self._items

    def getUsedItems(self):
        return self._itemsUsed

    def hasBoost(self):
        return self._boost

    def hasSuperBoost(self):
        return self._superBoost

    def isGhost(self):
        return self._ghost

    def hasShield(self):
        return self._shield

    def getX(self):
        return self._agent.x

    def getY(self):
        return self._agent.y
