import unittest
from src.algoritmit.testaa_saannollinen_lause import testaa_saannollinen_lause

class testtestaa_saannollinenlause(unittest.TestCase):
    def setUp(self):
        pass
        

    def test_merkkijono_tulostettavissa(self):
        merkkijono="chr(15)))"+"Ei pitaisi toimia"
        on_saannollinen_lause=testaa_saannollinen_lause(merkkijono)
        self.assertEqual(False, on_saannollinen_lause.on_validi)