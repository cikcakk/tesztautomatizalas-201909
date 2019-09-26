# SOAP webszolg�ltat�sok �s SoapUI gyakorlati feladatok

## Celsius to Fahrenheit converter

A http://www.learnwebservices.com/ oldalon megtal�lhat� egy webszolg�ltat�s,
mely k�pes celsius �s fahernheit k�z�tt v�ltani.
A WSDL dokumentuma megtal�lhat� a http://www.learnwebservices.com/services/tempconverter?wsdl c�men.

T�rk�pezd fel, hogy a webszolg�ltat�s h�ny oper�ci�t tartalmaz! Mindegyik oper�ci�ra �rj legal�bb egy
tesztesetet! Pr�b�lkozz boundary-value analysis-szel is!

## Locations alkalmaz�s

A http://www.learnwebservices.com/locations/ c�men megtal�lhat� egy kedvenc
helyeket nyilv�ntart� alkalmaz�s. Ez ny�jt SOAP webszolg�ltat�s API-t,
mely WSDL dokumentuma megtal�lhat� a http://www.learnwebservices.com/locations/services/locations?wsdl
c�men.

Ez tipikusan megval�s�tja a CRUD m�veleteket, �rj mind a n�gy m�velethez (list�z�s, l�trehoz�s,
m�dos�t�s, t�rl�s) teszteseteket! Gondolj azokra az �gakra is, amikor helytelen adatot adunk meg!
(Pl. �res, t�l kicsi vagy t�l nagy sz�m.)
Egy l�p�sb�l �ll� tesztesetek eset�n csak a l�trehoz�shoz tudunk korrekt tesztesetet l�trehozni,
hiszen a list�z�shoz el�felt�tel, hogy az alkalmaz�s egy adott �llapotban legyen. Ugyan�gy
a m�dos�t�sn�l �s a t�rl�sn�l is l�teznie kell azzal az azonos�t�val, ami alapj�n m�dos�tani vagy
t�r�lni akarunk.

Tervezz meg a list�z�sra, m�dos�t�sra �s t�rl�sre is t�bb l�p�sb�l �ll� teszteseteket
(csak �rd le). L�ttuk, hogy a Postman eset�n az egyik k�r�sb�l kellett adatot �tvinni a m�sik
k�r�sbe. �rd le sz�vegesen, hogy honnan kell adatot kiolvasni, �s hov� kell beilleszteni.
(Eml�kezz vissza, Postman eset�n a JSON v�laszb�l kellett kiolvasni az azonos�t�t, �s 
�t kellett vinni a k�vetkez� k�r�s URL-j�be!)

P�lda a k�vetkez� egy m�sik fikt�v banki rendszer eset�n, ami egy �tutal�st tesztelne.
L�trehozunk k�t sz�ml�t, az els�re utalunk 200 egys�get, majd az els�r�l �tutalunk 50 egys�get a m�sodikra.
Azt kell ellen�rizni, hogy a sz�ml�kat list�zva az els�n 150, a m�sodikon 50 egys�g lesz.

```
Teszt l�p�sek:

Meg kell h�vni a "createAccount" oper�ci�t, aminek hat�s�ra a v�laszban a <account-number> tagen bel�l
megjelenik a l�trehozott banksz�mlasz�m (legyen ez a no1)
Meg kell h�vni a "createAccount" oper�ci�t m�g egyszer, aminek hat�s�ra a v�laszban a <account-number> 
tagen bel�l megjelenik a l�trehozott banksz�mlasz�m (legyen ez a no2)
Meg kell h�vni a "deposit" oper�ci�t, aminek az <dest-account-number> tagj�ben meg kell adni a no1 sz�mot,
valamint legyen az �sszeg 200 egys�g

Elv�rt eredm�ny:

Meg kell h�vni a "transfer" oper�ci�t, aminek az <src-account-number> tagj�ben meg kell adni a no1 sz�mot,
a <dest-account-number> tagj�ben meg kell adni a no2 sz�mot, �s a <amount> tagben meg kell adni 50-et
Meg kell h�vni a "listAccounts" oper�ci�t, az eredm�nyb�l ki kell v�lasztani azt a <account> taget,
melyben van egy gyermek <account-number> tag, aminek �rt�ke a no1, �s a <balance> tagben 150-nek kell 
szerepelnie.
Ahol az <account-number> tag �rt�ke no2, ott a <balance> tag �rt�ke 50 legyen
```

