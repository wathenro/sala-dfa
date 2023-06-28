class DFA_tila():
    def __init__(self,nimi) -> None:
        self.nimi=nimi      #tilan nimi
        self.NFA_tilat=[]   #mistä NFAn tiloista koostuu
        self.siirtymat={}   #siirtymät
        self.lopputila= False

class tee_DFA():
    def __init__(self,NFA) -> None:
        self.NFA=NFA                          # NFA josta DFA tehdään
        self.DFA=[]                           # DFA, lista tiloista
        self.nimi_indeksi=1                   # nimi ideksi DFAn tiloille
        alkutila=self.tee_alkutila(self.NFA)  # muodostetaan alkutila
        #print("DFAn Alkuitilassa seuraavat NFAn tilat")
        #for tilat in alkutila.NFA_tilat:
        #    print(tilat.nimi)
        self.muodosta_dfa(alkutila)           # muodostetaan DFA  


        
    def muodosta_dfa(self,alkutila):
        """Ei palauta arvoa
        
        Tehdään DFA objektin konstruktoriin annetusta NFAsta. DFA tallennetaan listana tila-objekteja joiden verkosto muodostaa DFAn.
        """
        
        DFA_jono=[]
        DFA_jono.append(alkutila)
        
        while len(DFA_jono)>0:
            if self.nimi_indeksi>1000:  #Pysäytetään, todennäköisimmin ollaan päättymättömässä silmukassa
                break
            #print("Pääsilmukka alkaa")
            kasiteltava_DFA_tila=DFA_jono.pop(0)
            #print("Nyt käsitellään DFA-tilaa nimeltä ", kasiteltava_DFA_tila.nimi)
            siirtymat_tilasta=[]
            for NFA_tila in kasiteltava_DFA_tila.NFA_tilat:        #kerätään kaikki ei-epsillon siirtymat joita dfa tilaan kuuluvilla nfa tiloilla on
                for siirtyma in NFA_tila.siirtymat:
                    if siirtyma!="eps" and (siirtyma not in siirtymat_tilasta):
                        siirtymat_tilasta.append(siirtyma)
            #print("Tilalle", kasiteltava_DFA_tila.nimi," löytyi siirtymät ",siirtymat_tilasta)
            

            for siirtyma in siirtymat_tilasta:         # jokaista kirjainta kohden tehdään uusi tila paitsi jos osoittaa itseensä
                tilat_joihin_siirrytty=[]      # kerätään muistiin kaikki tilat joihin siirtymä joko merkillä tai epsilonnilla jotta ei päädytä looppiin
                uusi_tila=DFA_tila(self.nimi_indeksi)  #luodaan uusi tila
                self.nimi_indeksi+=1                   # päivitetään nimi indeksiä
                
                
                for NFA_tila in kasiteltava_DFA_tila.NFA_tilat:    # käydään läpi kaikki yhteen DFA-tilaan sisältyvät NFA-tilat
                    if siirtyma not in NFA_tila.siirtymat.keys():
                        continue
                    #if NFA_tila.siirtymat[siirtyma] in kasiteltava_DFA_tila.NFA_tilat: # tilalla siirtyma itseensä
                    #    kasiteltava_DFA_tila.siirtymat[siirtyma]=kasiteltava_DFA_tila
                        #print("DFA tilalla siirtymä itseensä")
                    #else:
                    #uusi_tila=DFA_tila(self.nimi_indeksi)  #luodaan uusi tila
                    #self.nimi_indeksi+=1                   # päivitetään nimi indeksiä
                    """
                    Tämä koodi tässä johti silmukkaan koska tuli siirtymä joka johti tilaan joka oli jo olemassa. Tässä vielä jos tarvitsee palata
                    #self.DFA.append(uusi_tila)             # lisätään tila DFAhan
                    #DFA_jono.append(uusi_tila)
                    #kasiteltava_DFA_tila.siirtymat[siirtyma]=uusi_tila
                    #print("DFA Tilalla", kasiteltava_DFA_tila.nimi, " siirtymä DFA tilaan",kasiteltava_DFA_tila.siirtymat[siirtyma].nimi)
                    """
                    uusi_tila.NFA_tilat.append(NFA_tila.siirtymat[siirtyma]) #jos siirtymä sisältyy käsiteltävään NFA-tilaan lisätään se DFA-tilaan
                    tilat_joihin_siirrytty.append(NFA_tila.siirtymat[siirtyma]) #ja tiloihin jotka käsitelty
                    #print("Tilalla", uusi_tila.nimi, " koostumus ",uusi_tila.NFA_tilat)
                
                    for NFA_tila in uusi_tila.NFA_tilat:    # seuraavaksi käydään läpi epsillon-siirtymät
                        if len(NFA_tila.siirtymat["eps"])!=0:
                            kasittelyjono=[]
                            kasittelyjono.extend(NFA_tila.siirtymat["eps"])
                            #print("Käsittelyjono nyt",kasittelyjono)
                            while len(kasittelyjono)>0:
                                kasiteltava=kasittelyjono.pop(0)
                                #print("Käsitellään epsillon-siirtymää NFA-nodeen",kasiteltava.nimi)
                        

                                if kasiteltava not in tilat_joihin_siirrytty:
                                    uusi_tila.NFA_tilat.append(kasiteltava) #lisätään se DFA-tilaan
                                    tilat_joihin_siirrytty.append(kasiteltava) #ja tiloihin jotka käsitelty
                                    kasittelyjono.extend(kasiteltava.siirtymat["eps"]) # ja otetaan mukaan eps-siirtymat tästä tilasta"""
                    #Tarkistetaan kuuluuko saatu tila jo DFAhan. Jos kuuluu, siirtymä sinne, jos ei lisätään se sinne ja käsittelyjonoon.
                    tila_jo_DFAssa=False
                    for tila_DFAssa in self.DFA:
                        if uusi_tila.NFA_tilat==tila_DFAssa.NFA_tilat:
                            kasiteltava_DFA_tila.siirtymat[siirtyma]=tila_DFAssa
                            tila_jo_DFAssa=True
                            #print("Tila löytyi DFAsta")
                            break
                    if tila_jo_DFAssa==False:
                        self.DFA.append(uusi_tila)             # lisätään tila DFAhan
                        DFA_jono.append(uusi_tila)
                        kasiteltava_DFA_tila.siirtymat[siirtyma]=uusi_tila
                        """
                        Debuggausta varten
                        print("DFAn tilassa", uusi_tila.nimi," seuraavat NFAn tilat")
                        for tilat in uusi_tila.NFA_tilat:
                            print(tilat.nimi)
                        """



                        
        for tila in self.DFA:               #Merkitään lopputilat. Jos DFAssa oleva NFA tila sisältää lopputilan L, on sekin lopputila (=hyväksyvä tila)
            for NFA_tila in tila.NFA_tilat:
                if NFA_tila.nimi=="L":
                    tila.lopputila=True
                    #print("Löytyi lopputila joka on tila ", tila.nimi)
                    break

    def tee_alkutila(self,NFA):
        """DFA_tila
        
        Tehdään DFAn alkutila johon kerätään kaikki NFA tilat joihin NFAn alkutilasta pääsee epsillon-siirtymällä.
        """
        #print("Alkutilan teko alkaa")
        alkutila=DFA_tila("A")               #luodaan DFA alkutila nimeltä A
        kasiteltavat=[]                      #lista tiloille
        kasitellyt=[]
        kasiteltavat.append(NFA[0])          #NFAn ensimmäinen tila on alkutila
        while len(kasiteltavat)>=1:               # niin kauan kuin epsillon siirtymiä löytyy
            kasiteltava=kasiteltavat.pop(0)  # otetaan käsiteltävä tila
            kasitellyt.append(kasiteltava)
            for tila in kasiteltava.siirtymat["eps"]: #iteroidaan kaikki läpi kaikkien tilojen joihin epsilloin siirtymä
                if tila not in kasitellyt:
                    kasiteltavat.append(tila)    #lisätään nämä käsiteltävien listalle
            alkutila.NFA_tilat.append(kasiteltava) #ja lisätään tiloihin joista DFAn alkutila koostuu
        self.DFA.append(alkutila)            #lisätään alkutila DFA:han
        #print("Alkutilan teko päättyy")
        return alkutila                      #ja palautetaan se
        


    def kuuluuko_kieleen(self,merkkijono):
        """Boolean
        
        Tarkistetaan kuuluuko annettu merkkijono kieleen.
        """
        merkkijono=list(merkkijono)
        nykyinen_tila=self.DFA[0]
        if nykyinen_tila.lopputila==True and len(merkkijono)==0:
            return True

        while len(merkkijono)>0:
            siirtyma=merkkijono.pop(0)
            if siirtyma not in nykyinen_tila.siirtymat.keys():
                #print("Merkkiä vastaavaa siirtymää ei löydy. Ei kuulu kieleen")
                return False
            else:
                nykyinen_tila=nykyinen_tila.siirtymat[siirtyma]
        if nykyinen_tila.lopputila==True:
            #print("Merkkijono kuuluu kieleen")
            return True
        else:
            #print("Ei päädytty hyväksyvään tilaan, merkkijono ei kuulu kieleen")
            return False