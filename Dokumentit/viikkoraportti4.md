#Viikko 4

Koodin kirjoittaminen eteni hyvin verratuna edellisiin viikkoihin. Päivitettiin säännöllisen lauseen tarkastajaa testaa_saannollinen_lause.py niin että sen tunnistaa kaikki väärät lauseet mitä itse
keksin. Jotain saattaa vielä puuttua.

Kääntäjä säännöllisestä lauseesta NFAksi eteni melko hyvin. Toimii ilman sulkuja ja joillakin sulkuversioilla, ainakin sellaisilla joissa ensin on pelkkä merkki
ja | operaattorin jälkeen yksi sulkulause. Alkaa paljastua että sen sijaan että säännöllistä lausetta tulkataan vasemmalta oikealle, parempi tapa olisi voinut olla
jakaa käydä se ensin komponentteihin ja käydä ne läpi. Voi olla että tämä joudutaan vielä muuttamaan. NFA kirjoitetaan kuitenkin aluksi niin että se toimii vain yhdellä tai |-operaattorilla.
