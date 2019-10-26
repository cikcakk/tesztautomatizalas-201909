# Selenium IDE feladatok

## Els� teszteset

Az els� teszteset a hely felv�tel�t teszteli. Mivel sok adat lehet m�r
az adatb�zisban, egyedi nev� helyet kell felvenni. Ehhez egy timestampet
illeszt�nk a n�v v�g�re, mely az egyedis�get biztos�tja.

A nevet JavaScript-tel hozzuk l�tre, a k�vetkez� utas�t�ssal:

```javascript
return 'Viczian_' + Date.now();
```

Ellen�rizni azt akarjuk, hogy megjelenik-e a t�bl�zatban, �s a megfelel�
koordin�ta szerepel-e mellette. Ehhez egy olyan xpath kifejez�st kell �rni,
mely visszaadja azt a sort a t�bl�zatban, amelyben a gener�lt n�v szerepel,
�s abban kell venni a koordin�ta oszlop�t. Az xpath kifejez�s: `xpath=//tr[td[contains(text(), '${location_name}')]]/td[3]`

A teljes teszteset l�p�sei:

* B�ng�sz� megnyit�sa a `/locations/server` c�men
* N�v gener�l�sa: `Viczian_1572117939709`, ahol a sz�m egyedileg gener�lt
* �rlap kit�lt�se a n�vvel, �s a `10,10` koordin�t�val, majd elk�ld�se
* Visszaellen�rizz�k, hogy a koordin�ta `10.0,10.0` �rt�k�-e (vigy�zat, 
  a fel�leten megjelen�tve m�s a form�tuma, mint amit be kell �rni az �rlapon)

Ellen�rizd, hogy lefut-e a teszteset! Lehet, hogy m�dos�tanod kell, mert m�r nem a `Create location`
az els� gomb.

Eg�sz�tsd ki �gy a tesztesetet, hogy ellen�rizze le azt is, hogy megjelenik-e a `Location has saved.` sz�veg.

## Ellen�rz�ssel kapcsolatos tesztesetek

Seg�ts�g: �j tesztesetet felvenni a bal oldalon, a Tests leny�l� melletti `+` jellel lehets�ges.

* �rj olyan tesztesetet, mely azt ellen�rzi, hogy �res n�v eset�n megjelenik-e a hiba�zenet!
* �rj olyan tesztesetet, mely azt ellen�rzi, hogy �res koordin�t�k eset�n megjelenik-e a hiba�zenet!
* �rj olyan tesztesetet, mely azt ellen�rzi, hogy helytelen form�tum� koordin�t�k eset�n megjelenik-e a hiba�zenet!
* �rj olyan tesztesetet, mely azt ellen�rzi, hogy t�l alacsony, vagy t�l magas �rt�k eset�n hiba�zenet jelenik-e meg! 
Vigy�zz, itt az alkalmaz�s (sz�nd�kosan :) tartalmaz egy hib�t, amely rosszul ellen�rzi a koordin�t�kat. Tal�ld meg!

## M�dos�t�ssal kapcsolatos tesztesetek

�rj egy olyan tesztesetet, mely a m�dos�t�st teszteli.

* �j n�v gener�l�sa
* �rlap kit�lt�se, majd elk�ld�se
* Klikkeljen r� az `Edit` gombra (seg�ts�g: itt is egy xpath kell, az el�z� annyival t�bb, hogy nem a `td[3]`, amit ki kell keresni, hanem egy nagyobb index� oszlop, �s ebben van egy `a` tag, ami a link maga)
* M�dos�tsa a nevet egy �j gener�lt n�vre (ehhez vegy�l fel egy �j v�ltoz�t)
* Mentse el az �rlapot
* Ellen�rizze, hogy megjelenik-e a `Location has updated.` felirat
* Ellen�rizze, hogy a t�bl�zatban megjelenik-e az �j n�v

�rj egy tesztesetet a m�dos�t�sn�l is az �rlap ellen�rz�s�re (pl. helytelen n�v)!

## T�rl�ssel kapcsolatos tesztesetek

Mint a m�dos�t�sn�l, csak azzal a k�l�nbs�ggel, hogy azt kell ellen�rizni, hogy a t�bl�zatb�l elt�nik a megfelel� hely.
A `Location has deleted.` �zenetre is ellen�rizz r�! 

Ehhez a `assert element not present` parancsot haszn�ld! T�gy ellenpr�b�t is, azaz mikor nem ker�l t�rl�sre a hely (pl. a t�rl�sre klikkel�st
megjegyz�sbe teszted), elbukik a teszt.

Figyeld meg, hogy a felugr� ablakra milyen paranccsal v�laszol a Selenium?

## Nagyon nagyon neh�z feladat

Olvasd vissza az azonos�t�t, amely a n�v mellett megjelenik, t�rold el egy v�ltoz�ban, �s azzal k�rdezd le a sort,
�s l�tnod kell, hogy t�rl�s ut�n m�r nincs ilyen. (Ugyanezt m�dos�tsd a m�dos�t�sn�l is, hogy azonos�t� alapj�n keresse vissza!)

Az azonos�tot a k�vetkez�k�ppen kell visszaolvasni, majd ut�na ki�rni logba az ellen�rz�shez: 

```
store text | xpath=<<xpath kifejez�s>> | <<v�ltoz� neve>>

azaz pl.

store text | xpath=//h1 | title
echo | ${title}
```