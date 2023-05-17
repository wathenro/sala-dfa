# Määrittelydokumentti sala-dfa

**Sa**ännölliset **la**useet **DFA**ksi.

Projektissa toteutetaan säännöllisten lauseiden kääntäjän. Kääntäjä muuntaa annetun säännöllisen lauseen ensin epädeterministiseksi äärelliseksi automaatiksi (NFA), joka muunnetaan deterministiseksi äärelliseksi automaatiksi (DFA). DFAlle voidaan syöttää käyttäjän antama merkkijono. Jos DFA päätyy hyväksyvään tilaan annetulla merkkijonolla, annettu merkkijono kuuluu säännöllisen lauseen määrittämään kieleen. Jos päädytään mihin tahansa muuhun tilaan, merkkijono hylätään eikä se kuulu kieleen. Säännölliseen kieleen sisällytetään operaattorit | (unioni, tai),* (tähti, 1 tai useampi) ja + (0 tai useampi). Lisäksi se tunnistaa tyhjän merkkijonon ε ja sallii sulkumerkkien käytön.
Ohjelmalle syötetään yksinkertaisen graafisen käyttöliittymän kautta sekä säännöllinen lause että tutkittava merkkijono. Ohjelma tarkastaa molemmista hyväksyttävyyden. Jos molemmat ovat hyväksyttäviä, ohjelma muodostaa ensin ensin NFAn, siitä DFAn ja syöttää sitten tutkittavan merkkijonon muodostetulle DFAlle. Sekä NFA että DFA toteutetaan verkkoina. Algoritmit säännöllisen lauseen muuntamiseksi NFAksi ja NFAn DFAksi ovat kuvattu viitteissä. Pikainen epätieteellinen verkkotiedonhaku osoittaa että näihin on olemassa muitakin algoritmeja. Saman tiedonhaun perusteella aikavaatimus säännöllisestä lauseesta NFAksi on toteutettavissa O(n) ja NFAsta DFAksi O(2^n). Lisäksi tarvitaan algoritmi joka annetun säännöllisen lauseen oikeellisuuden. 
Projektissa käytetään Python-ohjelmointikieltä. Mahdollisia kieliä projektien arviointiin ovat Pythonin lisäksi Java, C, Matlab, R, Haskell ja Basic. Projektin dokumentaatiossa käytetty kieli on suomi.
Matemaattisten tieteiden kandiohjelma, opintosuunta tietojenkäsittelyteoria.
Viitteet:
Salmela, L., Laskennan mallit luentomateriaali syksy 2022.
Sipser, M., Introduction to the Theory of Computation, Third Edition,
