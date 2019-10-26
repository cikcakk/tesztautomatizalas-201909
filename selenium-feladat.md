# Selenium IDE feladatok

## Elsõ teszteset

Az elsõ teszteset a hely felvételét teszteli. Mivel sok adat lehet már
az adatbázisban, egyedi nevû helyet kell felvenni. Ehhez egy timestampet
illesztünk a név végére, mely az egyediséget biztosítja.

A nevet JavaScript-tel hozzuk létre, a következõ utasítással:

```javascript
return 'Viczian_' + Date.now();
```

Ellenõrizni azt akarjuk, hogy megjelenik-e a táblázatban, és a megfelelõ
koordináta szerepel-e mellette. Ehhez egy olyan xpath kifejezést kell írni,
mely visszaadja azt a sort a táblázatban, amelyben a generált név szerepel,
és abban kell venni a koordináta oszlopát. Az xpath kifejezés: `xpath=//tr[td[contains(text(), '${location_name}')]]/td[3]`

A teljes teszteset lépései:

* Böngészõ megnyitása a `/locations/server` címen
* Név generálása: `Viczian_1572117939709`, ahol a szám egyedileg generált
* Ûrlap kitöltése a névvel, és a `10,10` koordinátával, majd elküldése
* Visszaellenõrizzük, hogy a koordináta `10.0,10.0` értékû-e (vigyázat, 
  a felületen megjelenítve más a formátuma, mint amit be kell írni az ûrlapon)

Ellenõrizd, hogy lefut-e a teszteset! Lehet, hogy módosítanod kell, mert már nem a `Create location`
az elsõ gomb.

Egészítsd ki úgy a tesztesetet, hogy ellenõrizze le azt is, hogy megjelenik-e a `Location has saved.` szöveg.

## Ellenõrzéssel kapcsolatos tesztesetek

Segítség: új tesztesetet felvenni a bal oldalon, a Tests lenyíló melletti `+` jellel lehetséges.

* Írj olyan tesztesetet, mely azt ellenõrzi, hogy üres név esetén megjelenik-e a hibaüzenet!
* Írj olyan tesztesetet, mely azt ellenõrzi, hogy üres koordináták esetén megjelenik-e a hibaüzenet!
* Írj olyan tesztesetet, mely azt ellenõrzi, hogy helytelen formátumú koordináták esetén megjelenik-e a hibaüzenet!
* Írj olyan tesztesetet, mely azt ellenõrzi, hogy túl alacsony, vagy túl magas érték esetén hibaüzenet jelenik-e meg! 
Vigyázz, itt az alkalmazás (szándékosan :) tartalmaz egy hibát, amely rosszul ellenõrzi a koordinátákat. Találd meg!

## Módosítással kapcsolatos tesztesetek

Írj egy olyan tesztesetet, mely a módosítást teszteli.

* Új név generálása
* Ûrlap kitöltése, majd elküldése
* Klikkeljen rá az `Edit` gombra (segítség: itt is egy xpath kell, az elõzõ annyival több, hogy nem a `td[3]`, amit ki kell keresni, hanem egy nagyobb indexû oszlop, és ebben van egy `a` tag, ami a link maga)
* Módosítsa a nevet egy új generált névre (ehhez vegyél fel egy új változót)
* Mentse el az ûrlapot
* Ellenõrizze, hogy megjelenik-e a `Location has updated.` felirat
* Ellenõrizze, hogy a táblázatban megjelenik-e az új név

Írj egy tesztesetet a módosításnál is az ûrlap ellenõrzésére (pl. helytelen név)!

## Törléssel kapcsolatos tesztesetek

Mint a módosításnál, csak azzal a különbséggel, hogy azt kell ellenõrizni, hogy a táblázatból eltûnik a megfelelõ hely.
A `Location has deleted.` üzenetre is ellenõrizz rá! 

Ehhez a `assert element not present` parancsot használd! Tégy ellenpróbát is, azaz mikor nem kerül törlésre a hely (pl. a törlésre klikkelést
megjegyzésbe teszted), elbukik a teszt.

Figyeld meg, hogy a felugró ablakra milyen paranccsal válaszol a Selenium?

## Nagyon nagyon nehéz feladat

Olvasd vissza az azonosítót, amely a név mellett megjelenik, tárold el egy változóban, és azzal kérdezd le a sort,
és látnod kell, hogy törlés után már nincs ilyen. (Ugyanezt módosítsd a módosításnál is, hogy azonosító alapján keresse vissza!)

Az azonosítot a következõképpen kell visszaolvasni, majd utána kiírni logba az ellenõrzéshez: 

```
store text | xpath=<<xpath kifejezés>> | <<változó neve>>

azaz pl.

store text | xpath=//h1 | title
echo | ${title}
```