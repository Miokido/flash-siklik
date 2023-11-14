import pytest

from src.api.fs.Vehicle import Vehicle


class TestFlashSiklikApi(object):
    """
        test de la classe vehicule
    """

    def testVehicule(self):
        vehiculeTest = Vehicle(1, 1, "test", "test", "test", 1)

        assert vehiculeTest.turn(-1) == False
        assert vehiculeTest.turn(0) == True
        assert vehiculeTest.turn(1) == True
        assert vehiculeTest.turn(2) == True
        assert vehiculeTest.turn(3) == True
        assert vehiculeTest.turn(4) == False

        assert vehiculeTest.boost(True) is None
        assert vehiculeTest.boost(False) is None

        assert vehiculeTest.useItem(-1) == False
        assert vehiculeTest.useItem(0) == True
        assert vehiculeTest.useItem(1) == True
        assert vehiculeTest.useItem(2) == True
        assert vehiculeTest.useItem(3) == True
        assert vehiculeTest.useItem(4) == False

        assert vehiculeTest.update() is None

        assert vehiculeTest.getItems() is None
        assert vehiculeTest.getUsedItems() is None
        assert vehiculeTest.hasBoost() == False
        assert vehiculeTest.hasSuperBoost() == False
        assert vehiculeTest.isGhost() == False
        assert vehiculeTest.hasShield() == False
        assert vehiculeTest.getX() == 0
        assert vehiculeTest.getY() == 0
