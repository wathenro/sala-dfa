from tkinter import Label,Button,Entry
from algoritmit.testaa_saannollinen_lause import testaa_saannollinen_lause
from algoritmit.testaa_merkkijono import testaa_merkkijono
from algoritmit.tee_NFA import tee_NFA
from algoritmit.tee_DFA import tee_DFA



class UI():
    """Käyttöliittymä sala-dfa ohjelmalle
    
    Attribuutit:
        window: tkinter main window
    """
    def __init__(self,window):
        """UI constructor
    
        Args:
            window: tkinter main window
        """
        self.window=window
        self.window.title("sala-dfa")
        self.window.geometry("600x200")
        
        self.teksti_saannollinen_lause=Label(self.window,text="Anna säännöllinen lause")
        self.teksti_saannollinen_lause.place(x=10,y=20)

        self.saannollinen_lause=Entry(self.window)
        self.saannollinen_lause.insert(0, "(a+b*)")
        self.saannollinen_lause.place(x=10,y=50)
       
        self.teksti_merkkijono=Label(self.window,text="Anna merkkijono")
        self.teksti_merkkijono.place(x=250,y=20)

        self.merkkijono=Entry(self.window)
        self.merkkijono.insert(0, "aaaab")
        self.merkkijono.place(x=250,y=50)

        design_button=Button(self.window, text='Suorita', command=self.suorita, width=10)
        """"design_button.config(bg="BLUE")"""
        design_button.place(x=10,y=90)


        self.palaute_kuvaus=Label(self.window,text="Merkkijono kuuluu kieleen K/E, säännöllisessä lauseessa virhe V, merkkijonoa ei voi analysoida EVVK")
        self.palaute_kuvaus.place(x=10,y=120)

        self.palaute=""
        self.palaute_laatikko=Entry(self.window)
        self.palaute_laatikko.insert(0, self.palaute)
        self.palaute_laatikko.place(x=10,y=150)


    def suorita(self):
        """ Kutsuu metodit säännöllisen lauseen oikeellisuuden testaamiseen, merkkijonon hyväksyttävyyden testaamiseen, 
        säännöllisen lauseen muuntoon NFAksi, NFAn muuntoon DFAksi, syöttää merkkijonon DFAlle, palauttaa tuloksen

        
        """
        try:
            saannollinen_lause=self.saannollinen_lause.get()
        except:
            saannollinen_lause=""

        try:
            merkkijono=merkkijono.get()
        except:
            merkkijono=""
        print(saannollinen_lause)
        if testaa_saannollinen_lause(saannollinen_lause).on_validi and testaa_merkkijono(merkkijono).on_validi:
            NFA=tee_NFA(saannollinen_lause)
            DFA=tee_DFA(NFA)
            if DFA.kuuluuko_kieleen(merkkijono):
                palaute="K"
            else:
                palaute="e"
        elif not testaa_saannollinen_lause(saannollinen_lause).on_validi:
            palaute="V"
        else:
            palaute="EVVK"
        
        
        self.palaute_laatikko.delete(0,40)
        self.palaute_laatikko.insert(0, palaute) 