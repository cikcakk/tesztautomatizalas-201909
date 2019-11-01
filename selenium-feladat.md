# Selenium IDE feladatok

## Első teszteset

Az első teszteset a hely felvételét teszteli. Mivel sok adat lehet már
az adatbázisban, egyedi nevű helyet kell felvenni. Ehhez egy timestampet
illesztünk a név végére, mely az egyediséget biztosítja.

A nevet JavaScript-tel hozzuk létre, a következő utasítással:

```javascript
return 'Viczian_' + Date.now();
```

Ellenőrizni azt akarjuk, hogy megjelenik-e a táblázatban, és a megfelelő
koordináta szerepel-e mellette. Ehhez egy olyan xpath kifejezést kell írni,
mely visszaadja azt a sort a táblázatban, amelyben a generált név szerepel,
és abban kell venni a koordináta oszlopát. Az xpath kifejezés: `xpath=//tr[td[contains(text(), '${location_name}')]]/td[3]`

A teljes teszteset lépései:

* Böngésző megnyitása a `/locations/server` címen
* Név generálása: `Viczian_1572117939709`, ahol a szám egyedileg generált
* Űrlap kitöltése a névvel, és a `10,10` koordinátával, majd elküldése
* Visszaellenőrizzük, hogy a koordináta `10.0,10.0` értékű-e (vigyázat, 
  a felületen megjelenítve más a formátuma, mint amit be kell írni az űrlapon)

Ellenőrizd, hogy lefut-e a teszteset! Lehet, hogy módosítanod kell, mert már nem a `Create location`
az első gomb.

Egészítsd ki úgy a tesztesetet, hogy ellenőrizze le azt is, hogy megjelenik-e a `Location has saved.` szöveg.

## Ellenőrzéssel kapcsolatos tesztesetek

Segítség: új tesztesetet felvenni a bal oldalon, a Tests lenyíló melletti `+` jellel lehetséges.

* Írj olyan tesztesetet, mely azt ellenőrzi, hogy üres név esetén megjelenik-e a hibaüzenet!
* Írj olyan tesztesetet, mely azt ellenőrzi, hogy üres koordináták esetén megjelenik-e a hibaüzenet!
* Írj olyan tesztesetet, mely azt ellenőrzi, hogy helytelen formátumú koordináták esetén megjelenik-e a hibaüzenet!
* Írj olyan tesztesetet, mely azt ellenőrzi, hogy túl alacsony, vagy túl magas érték esetén hibaüzenet jelenik-e meg! 
Vigyázz, itt az alkalmazás (szándékosan :) tartalmaz egy hibát, amely rosszul ellenőrzi a koordinátákat. Találd meg!

## Módosítással kapcsolatos tesztesetek

Írj egy olyan tesztesetet, mely a módosítást teszteli.

* Új név generálása
* Űrlap kitöltése, majd elküldése
* Klikkeljen rá az `Edit` gombra (segítség: itt is egy xpath kell, az előző annyival több, hogy nem a `td[3]`, amit ki kell keresni, hanem egy nagyobb indexű oszlop, és ebben van egy `a` tag, ami a link maga)
* Módosítsa a nevet egy új generált névre (ehhez vegyél fel egy új változót)
* Mentse el az űrlapot
* Ellenőrizze, hogy megjelenik-e a `Location has updated.` felirat
* Ellenőrizze, hogy a táblázatban megjelenik-e az új név

Írj egy tesztesetet a módosításnál is az űrlap ellenőrzésére (pl. helytelen név)!

## Törléssel kapcsolatos tesztesetek

Mint a módosításnál, csak azzal a különbséggel, hogy azt kell ellenőrizni, hogy a táblázatból eltűnik a megfelelő hely.
A `Location has deleted.` üzenetre is ellenőrizz rá! 

Ehhez a `assert element not present` parancsot használd! Tégy ellenpróbát is, azaz mikor nem kerül törlésre a hely (pl. a törlésre klikkelést
megjegyzésbe teszted), elbukik a teszt.

Figyeld meg, hogy a felugró ablakra milyen paranccsal válaszol a Selenium?

## Nagyon nagyon nehéz feladat

Olvasd vissza az azonosítót, amely a név mellett megjelenik, tárold el egy változóban, és azzal kérdezd le a sort,
és látnod kell, hogy törlés után már nincs ilyen. (Ugyanezt módosítsd a módosításnál is, hogy azonosító alapján keresse vissza!)

Az azonosítot a következőképpen kell visszaolvasni, majd utána kiírni logba az ellenőrzéshez: 

```
store text | xpath=<<xpath kifejezés>> | <<változó neve>>

azaz pl.

store text | xpath=//h1 | title
echo | ${title}
```