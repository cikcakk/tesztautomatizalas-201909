# Selenium WebDriver Pythonnal

[Hogyan gondolkozz úgy, mint egy informatikus: Tanulás Python 3 segítségével](https://mtmi.unideb.hu/pluginfile.php/554/mod_resource/content/1/thinkcspy3.pdf)

A feladatok esetén, ha a Locations alkalmazásra történik hivatkozás, a http://www.learnwebservices.com/locations/server
címet használd.

## Változódeklaráció, típusok

* Szintaktika/szemantika
* Megjegyzések
* Változó, típus
* Kulcsszavak

### Feladat

* A Locations alkalmazásban olvasd be Dobogókő koordinátáját! Írd ki a típusát?
* A Locations alkalmazásban olvasd be Alattyán azonosítóját! Írd ki a típusát!
* A Locations alkalmazásban olvasd be a 9277 azonosítójú település nevét! Írd ki a típusát!

## Típuskonverziós függvények

* `int()`, `float()`, `str()`

* Próbáld meg Bakonybánk azonosítóját egész számmá konvertálni, és írd ki a változó típusát!
* Próbáld meg Zsámbék koordinátáját lebegőpontos számmá konvertálni! Mi történik?

## Műveletek

* Operátor, operandus, precedencia
* `len()`
* Szeletelés
* `replace()`
* `upper()`
* `lower()`
* `split()`
* `in`

* Kérdezd le Velence és Báta azonosítóját, majd add össze!
* Keresd ki a 9876 azonosítójú település nevét, majd írd ki az első három karakterét!
* Keresd ki a 9898 azonosítójú település nevét, majd írd ki visszafele!
* Keresd ki a 9742 azonosítójú település nevét, majd írd ki a hosszát, hogy hány karakterből áll!
* Keresd ki a 11115 azonosítójú település nevét, majd írd ki a csupa nagy és csupa kisbetűvel, hogy hány karakterből áll!
* Keresd ki a 11116, 11117, 11118 azonosítójú település nevét, majd írd ki egymástól kötőjelekkel elválasztva!
* Írd ki Tolmács koordinátáit, de space-szel elválasztva, és tizedespont helyett tizedes vesszővel!
* Keresd ki a Tiszakerecseny és Tiszarád koordinátáit! Add értékül négy lebegőpontos változóval!
* Az előző két településnek vond ki egymásből a szélességi és hosszúsági koordinátáit!
* Írd ki, hogy a 11262 azonosítójú településben szerepel-e a `margit` szó (`True` vagy `False`!
* Bónusz: számold ki a két település távolságát km-ben!

### Saját függvények

* Írj egy függvényt, ami paraméterül kap egy nevet, és kiírja a település koordinátáját!
* Írj egy függvényt, ami paraméterül kap egy nevet, és visszaadja a település koordinátáját!
* Írj egy függvényt, mely paraméterül kap egy azonosítót, és kikeresi a nevet!
* Írj egy függvényt, mely paraméterül kap egy azonosítót, és kikeresi a koordinátáját!

## HTML komponensek

* Label
* Textarea
* Password
* Checkbox
* Hidden
* Reset

* Készíts el egy kedvenc hely létrehozása űrlapot!
* Minden űrlap mezőnek legyen címkéje!
* Lehessen megadni egy több soros hosszú leírást!
* Lehessen megadni egy jelszót, amivel lehet igazolni, hogy ott voltál a helyszínen!
* Be lehessen pipálni, hogy a hely publikus-e. Valamint egy másik, hogy ingyenes-e!
* Rejtett mező legyen, hogy mi a kitöltés helye, jelen esetben legyen beégetve, hogy `webes-urlap`
* Lehessen az űrlapot üríteni!
* Írj rá egy Selenium WebDriver szkriptet, ami kitölti az űrlapot!

## Feltételes utasítások

* Írj egy függvényt, mely a paraméterként megadott település nevének ismeretében megmondja, hogy szélességi koordinátája
 nagyobb-e mint 48!
* Írj egy függvényt, mely a paraméterként megadott település nevének ismeretében megmondja, hogy szélességi koordinátája
 48.2 és 48.4 közé esik-e!
* Írj egy függvényt, mely a paraméterként megadott település azonosítójának ismeretében megmondja, hogy hossza nagyobb-e mint
8 karakter!

## Ciklusok

* Vegyél fel `ZZZ_Sajátnév` névvel öt helyet!
* Vegyél fel `ZZZ_Sajátnév` névvel öt helyet, ahol a lat rendre 1, 2, 3, 4, 5, és a lon koordináta rendre 1, 4, 9, 16, 25!
* Írd ki a konzolra az összes nevet!

## Listák és táblázat komponens

* Hozz létre az űrlapon egy listát, hogy milyen tageket érdemes használni!
* Hozz létre az űrlapon egy táblázatot amin városokat lehet megadni, névvel, alapítás évével, irányítószámmal!
* Írj WebDriver szkriptet, mely lekéri a lista elemeit, és kiírja!
* Írj egy WebDriver szkriptet, mely lekéri a táblázat összes celláját, és kiírja, hogy összesen hány cellát talált!

## Programozási tételek

1. Összegzés tétele
2. Számlálás tétele
3. Szélsőérték keresés tétele
4. Eldöntés tétele

* Keresd ki a leghosszabb nevű települést!
* Keresd ki a leghosszabb és legrövidebb nevű települést, anélkül, hogy kétszer járnád be a listát!
* Számold meg, hány `Á` betűvel kezdődő település van!
* Keresd ki a legkeletebbi és legészakabbi települést!

## Komplexebb HTML komponensek

* Rádiógombok
* Select
* Többelemű select

* Bővítsd úgy az űrlapot, hogy legyenek benne rádiógombok, legördülő menü és többelemű select!
* WebDriverrel kérd le, töltsd ki!