import pytest

import os
import sys
__workdir__ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
__j2ldir__ = os.path.join(__workdir__, "src", "api")
sys.path.append(__workdir__)
sys.path.append(__j2ldir__)

from src.api.fs.Vehicle import Vehicle


class TestFlashSiklikApi(object):

    """
        test vehicle class
    """
    def test_vehicule(self):
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
