# Szorzótábla

Adott a http://www.jtechlog.hu/tesztautomatizalas-201909/szorzotabla.html
oldalon egy szorzótábla.

* Írj egy függvényt `multiply_with_form` néven, ami vár két számot,
és WebDriverrel meghívja az oldalt, és kitölti a két beviteli mezőt, megnyomja
a _Szoroz_ gombot, majd kiolvassa az értéket! Vigyázz, konvertáld át egész számmá az eredményt!
* Írj egy függvényt `multiply_with_table` néven, ami vár két számot,
és WebDriverrel meghívja az oldalt, és a táblázatból kikeresi a megfelelő értéket! Itt egy olyan XPath kifejezést kell összeállítani, amit úgy konkatenálsz össze, hogy mindkét szám szerepel benne.
* Írj egy függvényt `multiply` néven, ami vár két számot, és Pythonnal
összeszorozza!
* Írd meg a program fő részét, ami bekér két számot, majd mind a három függvényt meghívja, és kiírja, hogy az első és második eredmény egyezik-e (`True` vagy `False`)! Valamint kiírja, hogy a második és harmadik eredmény megegyezik-e.

# Alkalmazottak alkalmazás

A http://www.learnwebservices.com/empapp/employees.xhtml címen található egy
remekbeszabott alkalmazás, mely az alkalmazottakat tartja nyilván.

* Írj egy olyan függényt, mely paraméterként kap egy szót,
és az alapján szűri a táblázatot! A felső mezőbe kell beírni, majd
megnyomni a _Search_ gombot.
* Írj egy olyan függvényt, mely a paraméterként kapott azonosítójú
alkalmazottat kitörli!
* Írj egy olyan függvényt, mely a paraméterként kapott nevű
alkalmazottat kitörli!
* Írj egy olyan függvényt, mely kiírja, hogy hány alkalmazott van!
* Írj egy függvényt, ami magyarra vált, és egy másik függvényt, amely angolra
vált!
* Írj egy függvényt, mely kap egy paramétert, ez lesz az alkalmazott neve!
Megnyomja a _Create employee_ linket, majd kitölti a beviteli mezőt.
* (Nem kell megoldani, egyelőre kikapcsolva.) Írj egy függvényt, mely visszaolvassa a monogramot! (Vedd észre, ahogy
  írod be a nevet, írja ki a monogramot alá.)
* Írj egy függvényt, ami visszaolvassa a hibaüzenetet! (Pl. üres 
  névvel hívd az előző függvényt, majd ezt.)
* Írj egy függvényt, mely paraméterek alapján beírja a második képernyőn
  a kártyaszámot! (Ez az első beviteli mező.) Majd megnyomja a _Create employee_ 
  gombot.
* Írj egy függvényt, mely kap egy nevet és egy kártyaszámot, és a
  paraméterekkel meghívja az előző két függvényt!
* Írj egy függvényt, mely kap egy régi nevet és egy új nevet, és
  módosítja az alkalmazott nevét régiről az újra.