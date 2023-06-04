class tila():
    def __init__(self,alkutila=True,lopputila=True) -> None:
        self.alkutila=True
        self.lopputila=True
        self.siirtymat={}

class tee_NFA():
    def __init__(self,saannollinen_lause) -> None:
        self.NFA=True
        self.operaattorit=["(",")","+","|","*"]
        _NFA=[]
        nykyinen_tila=tila(True,True)
        _NFA.append(nykyinen_tila)
        self.muodostus_silmukka(nykyinen_tila,saannollinen_lause)
    def muodostus_silmukka(self,nykyinen_tila,saannollinen_lause):
        for indeksi in range(0,len(saannollinen_lause)):
            # Käydään saannollinen lause läpi kirjain kirjaimelta, katsotaan miten rekursiivisuus alkaa muodostumaan
            if saannollinen_lause[indeksi] not in self.operaattorit:
                if saannollinen_lause[indeksi+1]
                uusi_tila=tila(False,True)
                nykyinen_tila.lopputila=False
                nykyinen_tila.siirtymat[indeksi]=uusi_tila
                nykyinen_tila=uusi_tila
                break


    def 