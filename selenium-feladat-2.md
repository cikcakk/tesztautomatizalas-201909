# Selenium IDE feladatok 2.

Ahogy láthatjátok, a webes alkalmazások teszteléséhez igen tisztában kell
lenni a HTTP szabvánnyal, egy HTML oldal felépítésével, benne szereplő
tagekkel, attribútumokkal, valamint a belőle felépített DOM fával, és
rajta végzett XPath és CSS selector műveletekkel.

## HTML feladat 1.

Készíts egy `index.html` állományt, mely dokumentálni fogja a 
[Locations](http://www.learnwebservices.com/locations/server)
alkalmazásunk tesztelését!

Ne feledd, a HTML szabványt először dokumentumok leírására találták ki, aztán
jöttek rá, hogy alkalmzásokban is lehet használni!

A dokumentumokat oszd több fejezetre, használj alcímeket!
Írj bele pár mondatot az alkalmazás funkcionalitásáról! Mivel webes alkalmazás,
írj bele pár dolgot, melyet a HTTP szabványról tudsz, lehetőleg használj
listát! Helyezz el benne egy táblázatot, mely a tesztesetek azonosítóját,
címét és rövid leírását tartalmazza.

Adj stílust a dokumentumnak, használj színeket!

A végére helyezz el egy űrlapot, melybe meg lehet adni egy teszt futtatás
eredményét. Legyen egy beviteli mező a dátumnak, egy a futtató személy nevének,
egy a hosszának!

### Technológiai iránymutatások

Nézd meg a Locations alkalmazás forráskódját, és próbálj onnan ihletet 
meríteni!

* Használj `html`, `body`, `head`, `title` tageket!
* Címsorokhoz használj `h1`, `h2` tageket!
* Bekezdéshez `p` taget!
* Legyen egy link az alkalmazásra, használj `a` taget!
* Helyezz el egy képet, használj `img` taget!
* Űrlaphoz használj `form` és `input` tageket!
* Az űrlapnál tördelj `div` tag segítségével, emelj ki egy szöveget `span` segítségével!
* A css-re `link` taggel hivatkozz!
* Az űrlapoknál add meg a `name` attribútumok értékét

### Selenium IDE feladat - ciklus

Hozz létre véletlen számú saját helyet! Mindegyik neve kezdődjön a saját neveddel!

### Technológiai iránymutatás

Véletlenszámot (0 - 9 között) létrehozni JavaScripttel a következő kifejezéssel lehet:

```javascript
Math.floor(Math.random() * 10); 
```

Ezt futtasd le, majd értékét tárold le egy változóban. Ezután a `times` paraméterének
ezt a változót add meg. A ciklison belül generálj egy nevet, melyben szerepel 
egy timestamp.

### Selenium IDE feladat - számolás

Írj egy olyan XPath kifejezést, mely kiválasztja az összes neveddel kezdődő
sort! Mentsd el egy változóba, hogy ebből mennyi van!
Módosítsd az oldal címét úgy, hgoy kiírja, hogy mennyit talált!

### Technológiai iránymutatás

* Használd a `starts-with` függvényt!
* Van egy `store xpath count` parancs, mely lefuttat egy XPath kifejezést, mely több elemet választ ki, és eltárolja egy változóban, hogy ebből mennyi van.

A következő kifejezéssel módosíthatod a címet:

```javascript
document.querySelector("h1").innerHTML = "Found: " + ${count} 
```

Nagyon érdekes, hogy amennyiben a változót a stringen belül használod, nem működik, pl. így:

```javascript
document.querySelector("h1").innerHTML = "Found: ${count}"
```

(Ez nekem órákba került rájönni.)

### Selenium IDE feladat - nevek megkeresése

Írj egy tesztesetet, ami ciklusban végigmegy a neveddel kezdődő helyeken, és
kiírja azt a logba!

### Technológiai iránymutatás

* Xpath-szal kérdezd le, hogy mennyi van ilyen!
* Definiálnod kell egy változót, majd ezt a változót kell növelned a ciklusmagban (`execute script`)!
* A ciklus magjában az első XPath-t annyival kell bővíteni, hogy a változóval kell megadni, hogy 
hanyadik elemet adja vissza
* `echo`-t használj mindenütt a hibakereséshez

## Selenium IDE feladat - törlés ciklusban

Írj egy tesztesetet, ami ciklusban végigmegy a neveddel kezdődő helyeken, és
kitörli azokat!

### Technológiai iránymutatás

* Xpath-szal kérdezd le, hogy mennyi van ilyen!
* Ciklusban válaszd ki az elsőt, majd kattints a mellette lévő törlés gombra!


## Selenium IDE feladat - törlés kiszervezése

Szervezd ki a törlést egy külön tesztesetbe, és paraméterezve hívd!

### Technológiai iránymutatás

A tesztesetben használj változót, hogy hanyadikat törölje ki, és a hívó tesztesetben
pedig állítsd be a változót! Így használhatod utána pl. XPath-ban:

```
//tr[${index}]
```

## Selenium WebDriver feladatok

Külön `.py` állományokban írd meg a következőket:

* Írj olyan szkriptet, mely azt ellenőrzi, hogy üres név esetén megjelenik-e a hibaüzenet!
* Írd meg a módosítás tesztelését is Selenium WebDriverrel!
* Írd meg a törlés tesztelését is Selenium WebDriverrel!

### Technológiai iránymutatás

Így kell timestampet generálni a névbe:

```python
ts = time.time()
name = "viczian" + str(ts);
```

Így kell ellenőrizni, hogy az adott XPath kifejezéssel nincs elem:

```python
elements = driver.find_elements(By.ID, "grrrr")
assert len(elements) == 0
```

(Lekérdezi az összeset, de mivel egy sincs, ennek a hossza nulla.)