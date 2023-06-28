class testaa_saannollinen_lause():
    def __init__(self,saannollinen_lause) -> None:
        """Konstukstori
        
        Tutkitaan onko annettu säännöllinen lause oikein kirjoitettu
        """

        if len(saannollinen_lause)==0:
             saannollinen_lause=" "
        vasensulku=0
        oikeasulku=0
        oikea_jarjestys=True
        muuten_oikein=True
        operaattorit=["|","+","*"]
        # Tarkistetaan että sulut ovat oikein päin
        for merkki in saannollinen_lause:
                if merkki=="(":
                    vasensulku+=1
                if merkki==")":
                    oikeasulku+=1
                if oikeasulku>vasensulku:
                    oikea_jarjestys=False
                    break
        
        # Tarkistetaan että sulkuja on yhtä monta
        yhta_monta=True
        if not saannollinen_lause.count("(")==saannollinen_lause.count(")"):
            yhta_monta=False
        
        # Tarkistetaan ettei aloitus ole operaattori
        if saannollinen_lause[0] in operaattorit:
             muuten_oikein=False
        
        # Tarkistetaan ettei operaattoreita ole kahta peräkkäin
        for indeksi in range(1,len(saannollinen_lause)):
             if (saannollinen_lause[indeksi-1] in operaattorit and saannollinen_lause[indeksi] in operaattorit) and \
             not (saannollinen_lause[indeksi]=="|" and ((saannollinen_lause[indeksi-1]=="*" or saannollinen_lause[indeksi-1]=="+"))):
                  muuten_oikein=False
        if saannollinen_lause[-1]=="|":
             muuten_oikein=False
        
        # Tarkistetaan muut väärät yhdistelmät
        vaaria=["(|","|)","()"]
        for vaara in vaaria:
             if vaara in saannollinen_lause:
                  muuten_oikein=False
        
        # Ja vaaditaan vielä ettei mukaan ole eksynyt hassuja ja asiattomia merkkejä
        if saannollinen_lause.isprintable and oikea_jarjestys and yhta_monta and muuten_oikein:
             self.on_validi=True
        else:
             self.on_validi=False

        


        
        