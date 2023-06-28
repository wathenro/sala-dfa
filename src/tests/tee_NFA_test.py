import unittest
from src.algoritmit.tee_NFA import tila, tee_NFA
from src.algoritmit.tee_DFA import DFA_tila, tee_DFA


class testtee_NFA(unittest.TestCase):
    def setUp(self):
        self.DFA=tee_DFA(tee_NFA("(a|b)*b+").NFA)
        self.DFA2=tee_DFA(tee_NFA("a*").NFA)
        self.DFA3=tee_DFA(tee_NFA("(ab)*(qw)+|a").NFA)
        self.DFA4=tee_DFA(tee_NFA("(asdf)*jepjep(asdf)*").NFA)
        self.DFA5=tee_DFA(tee_NFA("ε|a").NFA)
    def test_testaa_b(self):
        kuuluuko=self.DFA.kuuluuko_kieleen("b")
        self.assertEqual(True, kuuluuko)

    def test_testaa_bb(self):
        kuuluuko=self.DFA.kuuluuko_kieleen("bb")
        self.assertEqual(True, kuuluuko)

    def test_testaa_ab(self):
        kuuluuko=self.DFA.kuuluuko_kieleen("ab")
        self.assertEqual(True, kuuluuko)

    def test_testaa_aaaaabab(self):
        kuuluuko=self.DFA.kuuluuko_kieleen("aaaaabab")
        self.assertEqual(True, kuuluuko)

    def test_testaa_aaaaababa(self):
        kuuluuko=self.DFA.kuuluuko_kieleen("aaaaababa")
        self.assertEqual(False, kuuluuko)

    def test_testaa_a(self):
        kuuluuko=self.DFA.kuuluuko_kieleen("a")
        self.assertEqual(False, kuuluuko)

    def test_testaa_NewBeetle(self):
        kuuluuko=self.DFA.kuuluuko_kieleen("NewBeetle")
        self.assertEqual(False, kuuluuko)

    def test_testaa_tyhja(self):
        kuuluuko=self.DFA.kuuluuko_kieleen("")
        self.assertEqual(False, kuuluuko)

    def test_testaa_tyhja2(self):
        kuuluuko=self.DFA2.kuuluuko_kieleen("")
        self.assertEqual(True, kuuluuko)

    def test_testaa_abqw(self):
        kuuluuko=self.DFA3.kuuluuko_kieleen("abqw")
        self.assertEqual(True, kuuluuko)

    def test_testaa_aba(self):
        kuuluuko=self.DFA3.kuuluuko_kieleen("aba")
        self.assertEqual(True, kuuluuko)

    def test_testaa_asdfasdfasdfjepjepasdf(self):
        kuuluuko=self.DFA4.kuuluuko_kieleen("asdfasdfasdfjepjepasdf")
        self.assertEqual(True, kuuluuko)

    def test_testaa_epsillon_a(self):
        kuuluuko=self.DFA5.kuuluuko_kieleen("")
        self.assertEqual(True, kuuluuko)

    def test_testaa_epsillon_a2(self):
        kuuluuko=self.DFA5.kuuluuko_kieleen("a")
        self.assertEqual(True, kuuluuko)

    def test_testaa_epsillon_aa(self):
        kuuluuko=self.DFA5.kuuluuko_kieleen("aa")
        self.assertEqual(False, kuuluuko)

    



    

    

        
        
                    
