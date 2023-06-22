class DFA_tila():
    def __init__(self,nimi) -> None:
        self.nimi=nimi      #tilan nimi
        self.NFA_tilat=[]   #mistä NFAn tiloista koostuu
        self.siirtymat={}   #siirtymät

class tee_DFA():
    def __init__(self,NFA) -> None:
        self.NFA=NFA                          # NFA josta DFA tehdään
        self.DFA=[]                           # DFA, lista tiloista
        self.nimi_indeksi=1                   # nimi ideksi DFAn tiloille
        alkutila=self.tee_alkutila(self.NFA)  # muodostetaan alkutila
        for tilat in alkutila.NFA_tilat:
            print(tilat.nimi)
        self.muodosta_dfa(alkutila)           # muodostetaan DFA  


        
    def muodosta_dfa(self,alkutila):
        print("Muodostus alkaa")
        DFA_jono=[]
        DFA_jono.append(alkutila)
        
        while len(DFA_jono)>0:
            print("Pääsilmukka alkaa")
            kasiteltava_DFA_tila=DFA_jono.pop(0)
            print(kasiteltava_DFA_tila.nimi)
            siirtymat_tilasta=[]
            for NFA_tila in kasiteltava_DFA_tila.NFA_tilat:        #kerätään kaikki ei-epsillon siirtymat joita dfa tilaan kuuluvilla nfa tiloilla on
                for siirtyma in NFA_tila.siirtymat:
                    if siirtyma!="eps" and (siirtyma not in siirtymat_tilasta):
                        siirtymat_tilasta.append(siirtyma)
            print("Tilalle löytyi siirtymät ",siirtymat_tilasta)
            
            
            tilat_joihin_siirrytty=[]                  # kerätään muistiin kaikki tilat joihin siirtymä joko merkillä tai epsilonnilla
                                                    # jotta ei päädytä luuppiin
            for siirtyma in siirtymat_tilasta:         # jokaista kirjainta kohden tehdään uusi tila
                uusi_tila=DFA_tila(self.nimi_indeksi)
                self.nimi_indeksi+=1                   # päivitetään nimi indeksiä
                self.DFA.append(uusi_tila)             # lisätään tila DFAhan
                DFA_jono.append(uusi_tila)
                kasiteltava_DFA_tila.siirtymat[siirtyma]=uusi_tila
                print("Tilalla", kasiteltava_DFA_tila.nimi, " siirtymä tilaan",kasiteltava_DFA_tila.siirtymat[siirtyma].nimi)
                
                for NFA_tila in kasiteltava_DFA_tila.NFA_tilat:    # käydään läpi kaikki yhteen DFA-tilaan sisältyvät NFA-tilat
                    if siirtyma in NFA_tila.siirtymat: # jos siirtymä sisältyy käsiteltävään NFA-tilaan
                        uusi_tila.NFA_tilat.append(NFA_tila.siirtymat[siirtyma]) #lisätään se DFA-tilaan
                        tilat_joihin_siirrytty.append(NFA_tila.siirtymat[siirtyma]) #ja tiloihin jotka käsitelty
                print("Tilalla", uusi_tila.nimi, " koostumus ",uusi_tila.NFA_tilat)
                    
                for NFA_tila in uusi_tila.NFA_tilat:    # seuraavaksi käydään läpi epsillon-siirtymät
                    if "eps" in NFA_tila.siirtymat:
                        kasittelyjono=[]
                        kasittelyjono.extend(NFA_tila.siirtymat["eps"])
                        print(kasittelyjono)
                        while len(kasittelyjono)>0:
                            kasiteltava=kasittelyjono.pop(0)
                            print("Käsitellään epsillon-siirtymää NFA-nodeen",kasiteltava.nimi)
                        

                            if kasiteltava not in tilat_joihin_siirrytty:
                                uusi_tila.NFA_tilat.append(kasiteltava) #lisätään se DFA-tilaan
                                tilat_joihin_siirrytty.append(kasiteltava) #ja tiloihin jotka käsitelty
                                kasittelyjono.extend(kasiteltava.siirtymat["eps"]) # ja otetaan mukaan eps-siirtymat tästä tilasta"""

    def tee_alkutila(self,NFA):
        """DFA_tila
        
        Tehdään DFAn alkutila johon kerätään kaikki NFA tilat joihin NFAn alkutilasta pääsee epsillon-siirtymällä.
        """
        print("Alkutilan teko alkaa")
        alkutila=DFA_tila("A")               #luodaan DFA alkutila nimeltä A
        kasiteltavat=[]                      #lista tiloille
        kasiteltavat.append(NFA[0])          #NFAn ensimmäinen tila on alkutila
        while len(kasiteltavat)>=1:               # niin kauan kuin epsillon siirtymiä löytyy
            kasiteltava=kasiteltavat.pop(0)  # otetaan käsiteltävä tila 
            for tila in kasiteltava.siirtymat["eps"]: #iteroidaan kaikki läpi kaikkien tilojen joihin epsilloin siirtymä
                kasiteltavat.append(tila)    #lisätään nämä käsiteltävien listalle
            alkutila.NFA_tilat.append(kasiteltava) #ja lisätään tiloihin joista DFAn alkutila koostuu
        self.DFA.append(alkutila)            #lisätään alkutila DFA:han
        print("Alkutilan teko päättyy")
        return alkutila                      #ja palautetaan se
        


    def kuuluuko_kieleen(self,merkkijono):
        return(True)