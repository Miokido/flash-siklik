import unittest

from src.api.fs.Vehicle import Vehicle


class TestFlashSiklikApi(unittest.TestCase):
    """
        test de la classe vehicule
    """

    def testVehicule(self):
        vehiculeTest = Vehicle(1, 1, "test", "test", "test", 1)
        self.assertTrue(vehiculeTest.turn(-1),False)
        self.assertTrue(vehiculeTest.turn(0),True)
        self.assertTrue(vehiculeTest.turn(1),True)
        self.assertTrue(vehiculeTest.turn(2),True)
        self.assertTrue(vehiculeTest.turn(3),True)
        self.assertTrue(vehiculeTest.turn(4),False)

        self.assertTrue(vehiculeTest.boost(True),None)
        self.assertTrue(vehiculeTest.boost(False),None)

        self.assertTrue(vehiculeTest.useItem(-1),False)
        self.assertTrue(vehiculeTest.useItem(0),True)
        self.assertTrue(vehiculeTest.useItem(1),True)
        self.assertTrue(vehiculeTest.useItem(2),True)
        self.assertTrue(vehiculeTest.useItem(3),True)
        self.assertTrue(vehiculeTest.useItem(4),False)

        self.assertTrue(vehiculeTest.update(),None)

        self.assertTrue(vehiculeTest.getItems(),None)
        self.assertTrue(vehiculeTest.getUsedItems(),None)
        self.assertTrue(vehiculeTest.hasBoost(),False)
        self.assertTrue(vehiculeTest.hasSuperBoost(),False)
        self.assertTrue(vehiculeTest.isGhost(),False)
        self.assertTrue(vehiculeTest.hasShield(),False)
        self.assertTrue(vehiculeTest.getX(),0)
        self.assertTrue(vehiculeTest.getY(),0)
