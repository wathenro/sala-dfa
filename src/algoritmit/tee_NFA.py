class tila():
    def __init__(self,nimi) -> None:
        """Konstruktori
        
        Tila-objeksi jossa sanakirjana siirtymät tilasta ja muuttujana tilan nimi.
        """
        self.siirtymat={}
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
        
        Etsii syötetystä lauseesta joka alkaa (-lla uloimman sulkulauseen. Esimerkiksi
        syötteen (asd*(sdds)*)*ads(sdfs)+ tulisi palauttaa (asd*(sdds)*)*
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
                if (lause_suluissa[indeksi+1]=="*" or lause_suluissa[indeksi+1]=="+"):
                    sulkulause+=lause_suluissa[indeksi+1]
                    return sulkulause
                else:
                    return sulkulause
                    
            

    def muodostus_silmukka(self,alkutila,lopputila,saannollinen_lause):
        """Ei palauta arvoa
        
        Pääsilmukka NFAn muodostamiselle. Saa arvoina alkutila ja lopputilan ja muodostaa näiden välille
        NFAn. Suluissa olevia osia kutsutaan rekursiolla.
        """
        edellinen_tila=alkutila
        nykyinen_tila=tila(self.nimi_indeksi)
        self.nimi_indeksi+=1
        edellinen_tila.siirtymat["eps_e"]=nykyinen_tila
        self.NFA.append(nykyinen_tila)
        indeksi=0

        while indeksi<len(saannollinen_lause):
            wanha=indeksi
            print(indeksi,"Tässä",saannollinen_lause[indeksi])
            #print(saannollinen_lause[indeksi])
            #print(len(self.NFA))


            # Jos ollaan säännöllisen lauseen viimeisessä merkissä, viimeistellään NFA
            if indeksi>=len(saannollinen_lause)-1:
                edellinen_tila=nykyinen_tila
                nykyinen_tila=tila(self.nimi_indeksi)
                self.nimi_indeksi+=1
                edellinen_tila.siirtymat[saannollinen_lause[indeksi]]=nykyinen_tila
                nykyinen_tila.siirtymat["eps_e"]=lopputila
                self.NFA.append(nykyinen_tila)
                break

            
                

            # Käydään saannollinen lause läpi kirjain kirjaimelta
            if saannollinen_lause[indeksi] not in self.operaattorit:
                if saannollinen_lause[indeksi+1] not in self.operaattorit:              #Katsotaan onko seuraava kirjain normaali merkki
                    edellinen_tila=nykyinen_tila                                        #jos on niin nykyisestä tulee edellinen tila
                    nykyinen_tila=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1                                     #ja tehdään uusi tila 
                    edellinen_tila.siirtymat[saannollinen_lause[indeksi]]=nykyinen_tila #johon siirtymä edellisestä tilasta
                    self.NFA.append(nykyinen_tila)
                    indeksi+=1
                    #print(indeksi,nykyinen_tila.siirtymat)
                    continue                                                               #ja siirrytään seuraavaan indeksiin 
                if saannollinen_lause[indeksi+1]=="*":
                    edellinen_tila=nykyinen_tila
                    nykyinen_tila=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    edellinen_tila.siirtymat["eps_e"]=nykyinen_tila #jos merkkeja 0
                    edellinen_tila.siirtymat[saannollinen_lause[indeksi]]=nykyinen_tila #siirto merkillä
                    nykyinen_tila.siirtymat["eps_t"]=edellinen_tila #toistoa monta kertaa
                    indeksi+=2 #hypätään tähti yli
                    self.NFA.append(nykyinen_tila)
                    if indeksi>=len(saannollinen_lause):
                        nykyinen_tila.siirtymat["eps_e"]=lopputila
                    #print(indeksi,nykyinen_tila.siirtymat)
                    continue #ja siirrytään seuraavaan indeksiin
                if saannollinen_lause[indeksi+1]=="+":
                    edellinen_tila=nykyinen_tila
                    nykyinen_tila=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    edellinen_tila.siirtymat[saannollinen_lause[indeksi]]=nykyinen_tila #siirto merkillä
                    nykyinen_tila.siirtymat["eps"]=edellinen_tila #toistoa monta kertaa
                    indeksi+=2             #hypätään plussa yli
                    self.NFA.append(nykyinen_tila)
                    if indeksi>=len(saannollinen_lause):
                        nykyinen_tila.siirtymat["eps_e"]=lopputila
                    continue      #ja siirrytään seuraavaan indeksiin
                if saannollinen_lause[indeksi+1]=="|": #tai operaattori
                    if saannollinen_lause[indeksi+2]!="(": #jos toinen vaihtoehto ei ole sulkulause
                        edellinen_tila=nykyinen_tila
                        nykyinen_tila=tila(self.nimi_indeksi)
                        self.nimi_indeksi+=1
                        edellinen_tila.siirtymat[saannollinen_lause[indeksi]]=nykyinen_tila #oikastaan vähän ja tehdään siirtymää samasta tilasta
                        edellinen_tila.siirtymat[saannollinen_lause[indeksi+2]]=nykyinen_tila
                        self.NFA.append(nykyinen_tila)
                        indeksi+=2
                        continue
                    else:
                        lause_suluissa=self.etsi_sulkulause(saannollinen_lause[indeksi+2:]) # jos toinen vaihtoehto on sulkulause
                        edellinen_tila=nykyinen_tila
                        nykyinen_tila=tila(self.nimi_indeksi)
                        self.nimi_indeksi+=1
                        if lause_suluissa[-1]=="*":
                            edellinen_tila.siirtymat[saannollinen_lause[indeksi]]=nykyinen_tila #siirrytään merkillä
                            self.muodostus_silmukka(edellinen_tila,nykyinen_tila,lause_suluissa[1:len(lause_suluissa)-2]) #ja läheteään sulkulause rekursioon
                            nykyinen_tila.siirtymat["eps_t"]=edellinen_tila
                            self.NFA.append(nykyinen_tila)
                            #print(indeksi)
                            indeksi=indeksi+2+len(lause_suluissa) #ja hypätään indeksissä eteenpäin
                            
                            #print(indeksi)
                            #indeksi+=8
                            continue
                if saannollinen_lause[indeksi+1]=="(":
                    print("Rivi 147")
                    edellinen_tila=nykyinen_tila
                    nykyinen_tila=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    edellinen_tila.siirtymat[saannollinen_lause[indeksi]]=nykyinen_tila
                    self.NFA.append(nykyinen_tila)
                    indeksi+=1
            if saannollinen_lause[indeksi]=="(":
                print("nyt mennaa")
                edellinen_tila=nykyinen_tila
                nykyinen_tila=tila(self.nimi_indeksi)
                self.nimi_indeksi+=1
                edellinen_tila.siirtymat["eps_e"]=nykyinen_tila
                self.NFA.append(nykyinen_tila)
                #Etsitään sulkulause
                lause_suluissa=self.etsi_sulkulause(saannollinen_lause[indeksi:]) 
                #print(lause_suluissa)
                #print(lause_suluissa[1:len(lause_suluissa)-2])
                edellinen_tila=nykyinen_tila
                nykyinen_tila=tila(self.nimi_indeksi)
                self.nimi_indeksi+=1
                if lause_suluissa[-1]=="*":
                    edellinen_tila.siirtymat["eps_e"]=nykyinen_tila #epsillon siirtymä jos 0 kpl
                    nykyinen_tila.siirtymat["eps_t"]=edellinen_tila # epsillon siirtymä takaisin
                    self.muodostus_silmukka(edellinen_tila,nykyinen_tila,lause_suluissa[1:len(lause_suluissa)-2]) #ja läheteään sulkulause rekursioon
                    self.NFA.append(nykyinen_tila)
                    indeksi=indeksi+1+len(lause_suluissa) #ja hypätään indeksissä eteenpäin
                    if indeksi>=len(saannollinen_lause):
                        nykyinen_tila.siirtymat["eps_e"]=lopputila
                if lause_suluissa[-1]=="+":
                    nykyinen_tila.siirtymat["eps_t"]=edellinen_tila #epsillon siirtymä eteenpäin
                    self.muodostus_silmukka(edellinen_tila,nykyinen_tila,lause_suluissa[1:len(lause_suluissa)-2]) #ja läheteään sulkulause rekursioon
                    self.NFA.append(nykyinen_tila)
                    indeksi=indeksi+1+len(lause_suluissa) #ja hypätään indeksissä eteenpäin
                    if indeksi>=len(saannollinen_lause):
                        nykyinen_tila.siirtymat["eps_e"]=lopputila
                if lause_suluissa[-1]=="|":
                    self.muodostus_silmukka(edellinen_tila,nykyinen_tila,lause_suluissa[1:len(lause_suluissa)-2]) #ja läheteään sulkulause rekursioon
                    lause_suluissa_2=self.etsi_sulkulause(saannollinen_lause[indeksi+1+len(lause_suluissa):])
                    self.muodostus_silmukka(self,edellinen_tila,nykyinen_tila,lause_suluissa_2[1:len(lause_suluissa_2)-2])
                    self.NFA.append(nykyinen_tila)
                    indeksi=indeksi+2+len(lause_suluissa)+len(lause_suluissa_2)
                    if indeksi>=len(saannollinen_lause):
                        nykyinen_tila.siirtymat["eps_e"]=lopputila
                    
                        
            """           
            # Tämä on edellisen toisto ja järjetön, mutta näin säännöllien lause voi alkaa sulkumerkillä. Korjataan.
            if saannollinen_lause[indeksi]=="(":
                    #Etsitään sulkulause
                    print("indeksi on ",indeksi)
                    lause_suluissa=self.etsi_sulkulause(saannollinen_lause[indeksi:]) 
                    edellinen_tila=nykyinen_tila
                    nykyinen_tila=tila(self.nimi_indeksi)
                    self.nimi_indeksi+=1
                    if lause_suluissa[-1]=="*":
                        edellinen_tila.siirtymat["eps_e"]=nykyinen_tila #epsillon siirtymä jos 0 kpl
                        nykyinen_tila.siirtymat["eps_t"]=edellinen_tila # epsillon siirtymä takaisin
                        self.muodostus_silmukka(edellinen_tila,nykyinen_tila,lause_suluissa[1:len(lause_suluissa)-2]) #ja läheteään sulkulause rekursioon
                        self.NFA.append(nykyinen_tila)
                        indeksi=indeksi+len(lause_suluissa) #ja hypätään indeksissä eteenpäin
                        print(indeksi)
                        if indeksi>=len(saannollinen_lause):
                            nykyinen_tila.siirtymat["eps_e"]=lopputila
                    if lause_suluissa[-1]=="+":
                        nykyinen_tila.siirtymat["eps_t"]=edellinen_tila #epsillon siirtymä eteenpäin
                        self.muodostus_silmukka(edellinen_tila,nykyinen_tila,lause_suluissa[1:len(lause_suluissa)-2]) #ja läheteään sulkulause rekursioon
                        self.NFA.append(nykyinen_tila)
                        indeksi=indeksi+len(lause_suluissa) #ja hypätään indeksissä eteenpäin
                        print(indeksi)
                        if indeksi>=len(saannollinen_lause):
                            nykyinen_tila.siirtymat["eps_e"]=lopputila
"""



            if wanha==indeksi: indeksi+=1000000 #Varmistetaan ettei jäädä ikuiseen luuppiin, poistetaan valmiista
        print("pois")

