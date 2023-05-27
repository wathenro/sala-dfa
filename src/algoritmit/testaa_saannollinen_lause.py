class testaa_saannollinen_lause():
    def __init__(self,saannollinen_lause) -> None:
        vasensulku=0
        oikeasulku=0
        oikea_jarjestys=True
        for merkki in saannollinen_lause:
                if merkki=="(":
                    vasensulku+=1
                if merkki==")":
                    oikeasulku+=1
                if oikeasulku>vasensulku:
                    oikea_jarjestys=False
                    break
        
        yhta_monta=True
        if not saannollinen_lause.count("(")==saannollinen_lause.count(")"):
            yhta_monta=False
        print(saannollinen_lause)
        if saannollinen_lause.isprintable and oikea_jarjestys and yhta_monta:
             self.on_validi=True
        else:
             self.on_validi=False

        


        
        