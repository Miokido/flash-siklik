from j2l.pytactx.agent import Agent
from src.api.fs import Vehicle


class IDeathArbiter:
    def isDead(self, vehicle: Vehicle):
        """
            this method returns true if the vehicle is dead
            :param vehicle: Vehicle
            :return: bool
        """
        pass

    def killVehicle(self, vehicle: Vehicle):
        """
            this method kills the vehicle
            :param vehicle: Vehicle
            :return: void
        """
        pass

    def checkIsDeathElseKill(self, vehicle: Vehicle, map: [[], []]):
        """
            this method checks if the vehicle is dead and kills it if it is not
            :param vehicle: Vehicle
            :return: void
        """
        pass

    def update(self):
        pass


class DeathArbiter(IDeathArbiter):
    def __init__(self, agent):
        self.__agent = agent

    def isDead(self, vehicle: Vehicle):
        """
            this method returns true if the vehicle is dead
            :param vehicle: Vehicle
            :return: bool
        """
        return vehicle.life <= 0

    def killVehicle(self, vehicle: Vehicle):
        """
            this method kills the vehicle
            :param vehicle: Vehicle
            :return: void
        """
        vehicle.life = 0

    def checkIsDeathElseKill(self, vehicle: Vehicle, map: [[], []]):
        """
            this method checks if the vehicle is dead and kills it if it is not
            :param vehicle: Vehicle
            :return: void
        """
        if self.isDead(vehicle) is False:
            if ((map[vehicle.x][vehicle.y] == 2 or map[vehicle.x][vehicle.y] == 1)
                    and vehicle.isGhost() is False and vehicle.hasShield() is False):
                self.killVehicle(vehicle)

    def killWeakAgents(self):
        map = self.__agent.map
        for agentName, agentAttributes in self.__agent.range.items():
            agentX = agentAttributes["x"]
            agentY = agentAttributes["y"]

            if map[agentY][agentX] > 0:
                self.__agent.rulePlayer(agentName, 'life', 0)
                self.__agent.ruleArena('delPlayer', [agentName])

    def update(self):
        self.killWeakAgents()
        self.__agent.update()
