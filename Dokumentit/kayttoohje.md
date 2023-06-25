# Käyttöohje

## Käynnistys

- Lataa repo zippinä tai mahdollinen release ja pura ne
- Siirry ohjelman hakemistoon
- Varmista että asennettuna ja käytössä on Pythonin tkinter-kirjasto. Mitä todennäköisimmin on.
- Ohjelma on tehty ja testattu Python 3.8.5 versiolla, joten se toiminee ainakin sillä ja uudemmilla.
- Käynnistä python src/index.py tai python3 src/index.py

## Käyttö

![Kuva käyttöliittymästä](https://github.com/wathenro/sala-dfa/blob/main/Dokumentit/kayttoliittyma.jpg)

Kuvassa yllä käyttöliittymä joka on melko yksiselitteinen. Säännöllisessä lauseessa voit käyttää kaikkia tulostettavia merkkejä, sulkumerkkejä ( ja ), sekä operaattoreita *, + ja |.

- \* nolla tai useampi
- \+ yksi tai useampi
- | tai

ε-merkki tulkitaan tyhjänä merkkinä.

Painamalla 'Suorita' ohjelma tarkastaa ensin annetun säännöllisen lauseen ja annetun merkkijonon oikeellisuuden, tekee sitten NFAn josta se tekee DFAn ja testaa DFAlla kuuluuko annettu merkkijono kieleen.
Tulos raportoidaan joko

- K kuuluu kielee
- E ei kuulu kieleen
- V säännöllisessä lauseessa virhe
- EVVK merkkijonoa ei voida analysoida
  

