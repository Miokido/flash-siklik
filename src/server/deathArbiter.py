from src.api.fs import Vehicle


class IDeathArbiter:
    def __init__(self):
        pass

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

    def checkIsDeathElseKill(self, vehicle: Vehicle):
        """
            this method checks if the vehicle is dead and kills it if it is not
            :param vehicle: Vehicle
            :return: void
        """
        pass

class DeathArbiter(IDeathArbiter):
    def __init__(self):
        super().__init__()

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

    def checkIsDeathElseKill(self, vehicle: Vehicle):
        """
            this method checks if the vehicle is dead and kills it if it is not
            :param vehicle: Vehicle
            :return: void
        """
        if self.isDead(vehicle) is False:
            self.killVehicle(vehicle)