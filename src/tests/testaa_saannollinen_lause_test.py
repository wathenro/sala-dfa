import unittest
from src.algoritmit.testaa_saannollinen_lause import testaa_saannollinen_lause

class testtestaa_saannollinenlause(unittest.TestCase):
    def setUp(self):
        pass
        

    def test_merkkijono_tulostettavissa(self):
        merkkijono="chr(15)))"+"Ei pitaisi toimia"
        on_saannollinen_lause=testaa_saannollinen_lause(merkkijono)
        self.assertEqual(False, on_saannollinen_lause.on_validi)
    
    def test_sulkeet_oikein(self):
        merkkijono="((sdf)))"
        on_saannollinen_lause=testaa_saannollinen_lause(merkkijono)
        self.assertEqual(False, on_saannollinen_lause.on_validi)

    def test_tyhja_kieli(self):
        merkkijono=""
        on_saannollinen_lause=testaa_saannollinen_lause(merkkijono)
        self.assertEqual(True, on_saannollinen_lause.on_validi)

    def test_operaattorit_vaarin_1(self):
        merkkijono="asd+*aa"
        on_saannollinen_lause=testaa_saannollinen_lause(merkkijono)
        self.assertEqual(False, on_saannollinen_lause.on_validi)

    def test_operaattorit_vaarin_2(self):
        merkkijono="asd()aa"
        on_saannollinen_lause=testaa_saannollinen_lause(merkkijono)
        self.assertEqual(False, on_saannollinen_lause.on_validi)

    def test_alkaa_operaattorilla(self):
        merkkijono="+asd*aa"
        on_saannollinen_lause=testaa_saannollinen_lause(merkkijono)
        self.assertEqual(False, on_saannollinen_lause.on_validi)

    def test_paattyy_unioniin(self):
        merkkijono="asd*aa|"
        on_saannollinen_lause=testaa_saannollinen_lause(merkkijono)
        self.assertEqual(False, on_saannollinen_lause.on_validi)

    
    