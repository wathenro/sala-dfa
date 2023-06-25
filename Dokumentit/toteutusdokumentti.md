# Toteutusdokumentti sala-dfa

Säännöllisen lauseen muodostama kieli on tunnistettavissa (epä-)deterministisellä äärellisellä automaatilla.
Ohjelman sala-dfa tarkoituksena on muuntaa annettu säännöllinen lause epädeterministiseksi äärelliseksi automaatiksi (non-deterministic finite automata, NFA),
muuntaa saatu NFA deterministiseksi äärelliseksi automaatiksi (determinstic finite automata, DFA) ja saadun DFAn avulla tunnistaa kuuluuko käyttäjän antama
merkkijono säännöllisen lauseen muodostamaan kieleen. 

Ohjelma kirjoitettiin Pythonilla. Graaffinen käyttöliittymä tehtii tkinter-kirjaston avulla. Käyttöliittymän koodi oli yksinkertainen ja helppo ymmärtää.

Käyttäjällä on mahdollista syöttää sekä säännöllinen lause että merkkijono jonka kuuluvuutta kieleen testataan muodostuneen DFAn avulla.
Ohjelma tarkastaa ensin luokkien testaa_saannollinen_lause ja testaa_merkkijono konstruktoreita käyttäen, että molemman ovat valideja prosessointiin.
Luokassa testaa_saannollinen lause testataan esimerkiksi, että kahta operaattoria kuten ** tai *+ ei ole peräkkäin. Luokka testaa_merkkijono on merkitykseltään todennäköisesti vähäinen,
sillä on varauduttu lähinnä siihen että syötetyssä merkkijonossa voisi olla elementtejä jotka kaatavat tai sekoittavat ohjelman.

Kun säännöllinen lause ja merkkijono on hyväksytty muodostetaan NFA luokassa tee_NFA syöttämällä säännöllinen lause sen konstruktoriin.
Luodaan NFA:lle 2 tilaa, alkutila ja lopputila. NFA:n tilat ovat luokan tila-objekteja joilla on nimi ja sanakirja siirtymat jossa hakusanana
on merkki tai epsillon ja arvoina toinen tila-objekti. Epsillon-hakusanan kohdalla arvona on lista tiloista. Varsinainen muodostuva NFA on
objektissa oleva lista NFA. Alkutila, lopputila ja säännöllinen lause syötetään luokan metodiin muodostus_silmukka. Tämä alkaa muodostamaan
NFAta lukien säännöllista lausetta vasemmalta oikealla. Sulkumerkin “(“ kohdatessaan metodi lähettää vielä analysoimatta olevan osion säännöllisestä
lauseesta ensin metodiin etsi_sulkulause, joka etsii suluissa olevan lauseen, esimerkiksi syötteellä (asd*(sdds)*)*ads(sdfs)+ se palauttaa (asd*(sdds)*).
Tämä saatu osio lähetetään rekursiivisesi metodiin muodostus_silmukka. Kun annettu säännöllinen lause on käyty läpi on NFA muodostunut luokan listaan NFA.
Säännöllisestä lauseesta NFAksi muodostaminen osoittautui projektin ylivoimaisesti vaikeimmaksi osuudeksi, enimmäkseen älyn puutteen vuoksi.
Kurssin Laskennan mallit luentomateriaali (2022) ja kurssin kirja [Sipser](http://staff.ustc.edu.cn/~huangwc/book/Sipser_Introduction.to.the.Theory.of.Computation.3E.pdf)
eivät kumpikaan oikein tarjonneet valmista algoritmia joka olisi suoraan voitu kirjoittaa Pythonille. Periaate kyllä esitetään mutta kuten sanottu,
äly ei riittänyt kirjoittamaan sitä algortmiksi. Lähdettiin kirjoittamaan algoritmia joka lukee säännöllistä lausetta merkki kerrallaan ja muodostaa NFAta matkan varrella.
Tätä oli suuria vaikeuksia saada toimimaan. Nettiä selaamalla törmättiin Thompsonin konstruktioon ja tästä saadut ideat saivat projektin eteenpäin. Jos käännös säännöllisestä
lauseesta NFAksi olisi toteutettu kokonaan Thompsonin konstruktiolla olisi koodaaminen pitänyt aloittaa täysin alusta, pienen pähkimisen jälkeen todettiin että tähän ei ryhdytä.
Lopullinen algoritmi on siis omaa tuotantoa voimakkailla vaikutteilla. Varmasti joku on tehnyt vastaavan aiemminkin.
[Thompsonin konstruktiolla](https://en.wikipedia.org/wiki/Thompson%27s_construction) tehty NFA pystyy tunnistamaan merkkijonon lineaarisessa ajassa, uskoakseni sala-dfa pystyy
melko lailla samaan, koska mihinkään ei varsinaisesti haarauduta josta joutusi palaamaan takaisin.

NFAn muunnos DFAksi tehdään Laskennan mallit luentomateriaalin ja Sipserin kirjan esittämän algortimin mukaan luokassa tee_DFA jonka konstruktorin syötteenä saatu NFA.
Ymmärtääkseni tapa on melko lailla [tämä](https://en.wikipedia.org/wiki/Powerset_construction). Luodaan alkutila metodilla tee_alkutila NFAn alkutilasta ja sen epsillon-siirtymistä
ja aloitetaan siitä tilasta luomaan DFAta metodilla muodosta_dfa. Tämä oli loppujen lopuksi kohtuullisen helppo totetuttaa ja lopulta toimiessaan paljasti monia bugeja
tee_NFAn tuottamissa automaateissa. Aikavaatimus ei liene lineaarinen koska kun uusi DFA tila on luotu, on pakko käydä läpi jo muodostetut tilat.
Jos tila on olemassa, luodaan siirtymä siihen eikä uutta tilaa lisätä DFAhan tai käsittelyjonoon. Jos näin ei tehtäisi päädyttäisiin mahdollisesti loputtomaan silmukkaan.

Kun testataan kuuluuko annettu merkkijono säännöllisen lauseen muodostamaan kieleen kutsutaan tee_DFA objektin metodia kuuluuko_kieleen. Tässä melko yksinkertaisesti luetaan merkki kerrallaan
ja siirrytään, jos pystytään, sen määräämään tilaan. Jos ei pystytä, merkkijono ei kuulu kieleen. Jos merkkijonon päätyttyä ollaan päädytty tilaan joka on lopputila, merkkijono kuuluu kieleen.

Ohjelmaa voisi kehittää tarpeen vaatiessa vaikka miten. Objekti tee_NFA olisi tehtävissä Thompsonin konstruktiolla, ja jos nyt lähtisin kirjoittamaan sitä alusta asti se todennäköisesti onnistuisi.
Haasteena olisi saada rekursiolla luodut osa-automaatit yhteen, mutta tämäkin on alkanut hahmottumaan. Kaiken tulostuksen voisi ohjata käyttöliittymäikkunaan, samoin kuin mahdollistaa luotujen
automaattien visualisointi. Koodissa on nyt poiskommentoituna osuudet jolla automaatit saa tulostettua konsoliin.

