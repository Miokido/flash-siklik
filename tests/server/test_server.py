import pytest

import os
import sys
__workdir__ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
__j2ldir__ = os.path.join(__workdir__, "src", "api")
sys.path.append(__workdir__)
sys.path.append(__j2ldir__)



class TestServer(object):

    """
        test serveur
    """

