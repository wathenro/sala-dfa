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
        edellinen_tila=alkutila
        nykyinen_tila=tila(self.nimi_indeksi)
        self.nimi_indeksi+=1
        edellinen_tila.siirtymat["eps"].append(nykyinen_tila)
        self.NFA.append(nykyinen_tila)

        indeksi=0

        while True:
           
            # Tyhjä kieli
            if saannollinen_lause=="":
                nykyinen_tila.siirtymat["eps"].append(lopputila)
                break
            #Säännöllinen lause läpikäyty, poistu
            if indeksi>=len(saannollinen_lause):
                nykyinen_tila.siirtymat["eps"].append(lopputila)
                break
            
            # Käydään saannollinen lause läpi kirjain kirjaimelta
            if saannollinen_lause[indeksi] not in self.operaattorit:
                edellinen_tila=nykyinen_tila #jos on niin nykyisestä tulee edellinen tila
                nykyinen_tila=tila(self.nimi_indeksi) #ja tehdään uusi tila
                self.nimi_indeksi+=1
                if saannollinen_lause[indeksi]=="ε":
                    edellinen_tila.siirtymat["eps"].append(nykyinen_tila) #epsillon siirtymä
                else:
                    edellinen_tila.siirtymat[saannollinen_lause[indeksi]]=nykyinen_tila #siirtymä edellisestä tilasta merkillä
                self.NFA.append(nykyinen_tila)
                indeksi+=1 #seuraavaan merkkiin
                continue

            if saannollinen_lause[indeksi]=="*": # *-operaattori
                # edellinen_tila.siirtymat["eps"].append(nykyinen_tila) #jos merkkeja 0 (vanha tn väärä versio jossa vain tämä)
                nykyinen_tila.siirtymat["eps"].append(edellinen_tila) #toistoa monta kertaa
                nykyinen_tila=tila(self.nimi_indeksi) #korjattu
                self.nimi_indeksi+=1
                self.NFA.append(nykyinen_tila)
                edellinen_tila.siirtymat["eps"].append(nykyinen_tila)
                indeksi+=1 #seuraavaan merkkiin
                continue

            if saannollinen_lause[indeksi]=="+": # +-operaattori
                nykyinen_tila.siirtymat["eps"].append(edellinen_tila) #toistoa monta kertaa
                indeksi+=1 #seuraavaan merkkiin
                continue

            if saannollinen_lause[indeksi]=="|": # |-operaattori
                if saannollinen_lause[indeksi+1]!="(": #jos toinen vaihtoehto ei ole sulkulause
                    if saannollinen_lause[indeksi+1]=="ε":
                        edellinen_tila.siirtymat["eps"].append(nykyinen_tila) #epsillon siirtymä
                    else:
                        edellinen_tila.siirtymat[saannollinen_lause[indeksi+1]]=nykyinen_tila #oikastaan vähän ja tehdään siirtymää samasta tilasta
                    indeksi+=2 #seuraavaan merkkiin
                    continue
                else:
                    lause_suluissa=self.etsi_sulkulause(saannollinen_lause[indeksi+1:]) # jos toinen vaihtoehto on sulkulause
                    self.muodostus_silmukka(edellinen_tila,nykyinen_tila,lause_suluissa[1:len(lause_suluissa)-1]) #ja läheteään sulkulause rekursioon
                    indeksi+=(1+len(lause_suluissa)) #seuraavaan merkkiin
                    continue

            if saannollinen_lause[indeksi]=="(": # sulkulause
                edellinen_tila=nykyinen_tila
                nykyinen_tila=tila(self.nimi_indeksi)
                self.nimi_indeksi+=1
                edellinen_tila.siirtymat["eps"].append(nykyinen_tila) #siirrytään sulkulauseeseen, tarvitaan jotta *,+,| operaattorien toteutus toimii
                self.NFA.append(nykyinen_tila)
                #Etsitään sulkulause
                lause_suluissa=self.etsi_sulkulause(saannollinen_lause[indeksi:]) 
                edellinen_tila=nykyinen_tila
                nykyinen_tila=tila(self.nimi_indeksi) # nyt on tehty tilat joiden välillä sulkulauseen tilat tulevat
                self.nimi_indeksi+=1
                self.NFA.append(nykyinen_tila)
                self.muodostus_silmukka(edellinen_tila,nykyinen_tila,lause_suluissa[1:len(lause_suluissa)-1])
                indeksi+=(len(lause_suluissa)) #seuraavaan merkkiin
                continue
