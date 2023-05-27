import unittest
from src.algoritmit.testaa_merkkijono import testaa_merkkijono

class testtestaa_merkkijono(unittest.TestCase):
    def setUp(self):
        pass
        

    def test_merkkijono_tulostettavissa(self):
        merkkijono=chr(15)+"Ei pitaisi toimia"
        tulostettavissa=testaa_merkkijono(merkkijono)
        self.assertEqual(False, tulostettavissa.on_validi)

