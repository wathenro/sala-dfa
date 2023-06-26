class tila():
    def __init__(self,nimi) -> None:
        """Konstruktori
        
        Tila-objeksi jossa sanakirjana siirtymät tilasta ja muuttujana tilan nimi.
        """
        self.siirtymat={}
        self.siirtymat["eps"]=[]
        self.nimi=nimi

class tee_NFA():
    def __init__(self,saannollinen_lause) -> None:
        """Konstruktori
        
        Tekee NFAn hyväksytystä säännöllisestä lauseesta
        """
        self.operaattorit=["(",")","+","|","*"]
        self.NFA=[] # Tämä on itse NFA, lista johon kerätään tila-objektit
        alkutila=tila("A")
        lopputila=tila("L")
        self.NFA.append(alkutila)
        self.NFA.append(lopputila)
        self.nimi_indeksi=1
        self.muodostus_silmukka(alkutila,lopputila,saannollinen_lause)
        
    def etsi_sulkulause(self,lause_suluissa):
        """Palauttaa stringin
        
        Etsii syötetystä lauseesta joka alkaa (-lla ensimmäisen sulkulauseen. Esimerkiksi
        syötteen (asd*(sdds)*)*ads(sdfs)+ tulisi palauttaa (asd*(sdds)*)
        """
        vasen_sulku=0
        oikea_sulku=0
        sulkulause=""
        for indeksi in range(0,len(lause_suluissa)):
            if lause_suluissa[indeksi]=="(":
                vasen_sulku+=1
                sulkulause=sulkulause+lause_suluissa[indeksi]
            if lause_suluissa[indeksi]!="(" and lause_suluissa[indeksi]!=")":
                sulkulause=sulkulause+lause_suluissa[indeksi]
            if lause_suluissa[indeksi]==")":
                oikea_sulku+=1
                sulkulause=sulkulause+lause_suluissa[indeksi]
            if vasen_sulku==oikea_sulku: #jos oikeita ja vasempia sulkuja on yhtä paljon, on koossa yksi kokonaisuus
                return sulkulause
                    
            

    def muodostus_silmukka(self,alkutila,lopputila,saannollinen_lause):
        """Ei palauta arvoa
        
        Pääsilmukka NFAn muodostamiselle. Saa arvoina alkutila ja lopputilan ja muodostaa näiden välille
        NFAn. Suluissa olevia osia kutsutaan rekursiolla.
        """
        tila4=alkutila
        indeksi=0
        edellinen=""

        while True:
           
            # Tyhjä kieli
            if saannollinen_lause=="":
                alkutila.siirtymat["eps"].append(lopputila)
                break
 
            #Säännöllinen lause läpikäyty, poistu
            if indeksi>=len(saannollinen_lause):
                tila4.siirtymat["eps"].append(lopputila)
                break
            
            # Käydään saannollinen lause läpi kirjain kirjaimelta
            if saannollinen_lause[indeksi] not in self.operaattorit:
                if edellinen!="|":
                    tila1=tila4
                    tila2=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    tila1.siirtymat["eps"].append(tila2)
                    self.NFA.append(tila2)

                    tila3=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    self.NFA.append(tila3)

                    tila4=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    self.NFA.append(tila4)
                    tila3.siirtymat["eps"].append(tila4)
                if saannollinen_lause[indeksi]=="ε":
                    tila2.siirtymat["eps"].append(tila3)
                else:
                    tila2.siirtymat[saannollinen_lause[indeksi]]=tila3
                edellinen=saannollinen_lause[indeksi]
                indeksi+=1

                continue

            if saannollinen_lause[indeksi]=="*": # *-operaattori
                tila3.siirtymat["eps"].append(tila2)
                tila2.siirtymat["eps"].append(tila4)
                edellinen=saannollinen_lause[indeksi]
                indeksi+=1 #seuraavaan merkkiin
                continue

            if saannollinen_lause[indeksi]=="+": # +-operaattori
                tila3.siirtymat["eps"].append(tila2)
                edellinen=saannollinen_lause[indeksi]
                indeksi+=1 #seuraavaan merkkiin
                continue

            if saannollinen_lause[indeksi]=="|": # |-operaattori
                tila2=tila(self.nimi_indeksi)
                self.nimi_indeksi+=1
                tila1.siirtymat["eps"].append(tila2)
                self.NFA.append(tila2)

                tila3=tila(self.nimi_indeksi)
                self.nimi_indeksi+=1
                self.NFA.append(tila3)
                tila3.siirtymat["eps"].append(tila4)

                edellinen=saannollinen_lause[indeksi]
                indeksi+=1
                continue

            if saannollinen_lause[indeksi]=="(": # sulkulause
                if edellinen!="|":
                    tila1=tila4
                    tila2=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    tila1.siirtymat["eps"].append(tila2)
                    self.NFA.append(tila2)

                    tila3=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    self.NFA.append(tila3)

                    tila4=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    self.NFA.append(tila4)
                    tila3.siirtymat["eps"].append(tila4)
                lause_suluissa=self.etsi_sulkulause(saannollinen_lause[indeksi:])
                self.muodostus_silmukka(tila2,tila3,lause_suluissa[1:len(lause_suluissa)-1])
                edellinen=saannollinen_lause[indeksi]
                indeksi+=(len(lause_suluissa))
                continue
