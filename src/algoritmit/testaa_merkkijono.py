class testaa_merkkijono():
    def __init__(self,merkkijono) -> None:
        """Konstruktori
        
        Tarkastetaan että syötetty merkkijono on analyysikelpoinen.
        """
        self.on_validi=merkkijono.isprintable()
        