## Webes alkalmazások

* Böngésző a kliens
	* Microsoft Internet Explorer, Microsoft Edge
	* Mozilla Firefox
	* Google Chrome
* Mivel böngésző mindenütt telepített, megszűnnek a telepítési/frissítési problémák
* Vékony kliensnek is nevezik, utalva arra, hogy a logika főleg szerver oldalon van
	* Elegendő csak ott frissíteni
* Háttérben a HTTP, HTML, CSS, JavaScript technológiák

---

## URL

* Uniform Resource Locator
* Interneten található erőforrások (szöveges tartalmak, képek, hangfájlok, videók) egyedi azonosítására
* Felépítése
	* Protokoll
	* Tartománynév
	* Port
	* Elérési út

---

## HTTP(S) protokoll

* 1999-ben kiadott RFC 2616 definiálja a HTTP/1.1-et (W3C szervezet)
* 2015-ben leváltott a HTTP/2.0-ás verzió, amit az RFC 7540 definiál
* Kliens-szerver kommunikáció
* Kliens tipikusan böngésző
* Kérés-válasz alapú protokoll
* Szöveges
* Fejléc, törzs
* Állapotmentes
* (S): secure - SSL alapú titkosítás
* Eszközök: Böngésző Fejlesztői eszköztár

---

## HTTP kérés

```
Accept: text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3
Cache-Control: max-age=0
Connection: keep-alive
Cookie: _ga=GA1.2.1967894445.149906973…yis3b41advsb3cwc3b3rk; _gat=1
Host: www.learnwebservices.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/57.0

GET http://www.learnwebservices.com/ HTTP/1.1
```

---

## HTTP válasz

```
HTTP/1.1 200 OK
Cache-Control: no-cache
Pragma: no-cache
Content-Type: text/html; charset=utf-8
Content-Encoding: gzip
Server: Kestrel
Date: Fri, 09 Aug 2019 11:45:51 GMT

<!DOCTYPE html>
<html lang="hu">
<head>
  <!-- ... -->
</head>
<body>
  <!-- ... -->
</body>
</html>
```

---

## Hivatkozott erőforrások

* CSS
* JavaScript
* Képek (tipikusan gif, jpg, svg formátumban)
	* Formátumok közötti különbségek

---

## Státuszkódok

* `200 OK`
* `302 Found`, lsd. később
* `304 Not Modified`, lsd. később
* `400 Bad Request`
* `401 Unauthorized`
* `403 Forbidden`
* `404 Not Found`
* `500 Internal Server Error`

---

## HTTP paraméterek

* Kérdőjellel (`?`) elválasztva
* Egymástól `&` karakterrel elválasztva
* URL encoding

http://www.learnwebservices.com/search.aspx?filter=javax&date=2017.12.01.&chkIT=true&chkOffice=true

http://www.learnwebservices.com/search.aspx?filter=alma%20k%C3%B6rte&date=0&chkIT=true&chkOffice=true

---

## Cache

* `Cache-Control`
	* `Cache-Control` fejléc (mp-ben), az adott tartalmat meddig lehet tárolnia lokálisan a böngészőnek
* `If-Modified-Since`
	* Kliens küldi, kéri a szervert, hogy csak akkor adjon vissza tartalmat, ha módosult azóta
	* `304 Not Modified`

---

## Mime-type

* `Content-Type` header
* Néhány: `text/plain`, `text/html`, `text/javascript`, `text/CSS`, `image/gif`, `image/jpeg`, `application/vnd.ms-excel` (`vnd` - vendor - nem szabványos)

http://www.learnwebservices.com/download.aspx?src=tanfolyam_jelentkezes_Learnwebservices.doc

```
Content-Type: application/msword
```

---

## Űrlapok

* `POST` metódus

```
POST /contact.aspx HTTP/1.1
Host: http://www.learnwebservices.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/57.0

UserName=demo@example.com&Password=password
```

---

## Cookie

* Szerver hozza létre
* Böngésző tárolja, és minden kéréskor visszaküldi a szervernek
* Csak ugyanannak a szervernek küldheti vissza
* Használata:
	* Pl. nyelv, pénznem (miben írja ki a webáruház az árakat)
	* Session követés (lsd. később)

---

## Állapotmentesség, session

* Két kérés között nincs kapcsolat
* Session (munkamenet): "felhasználónkénti" szerver oldali tárterület egyedi azonosítóval
* Azonosítót leküldi a szerver cookie-ban, melyet a kliens minden kéréssel visszaküld
* Timeout

---

## Átirányítás

* `GET` paraméterek, hossz limit
* `POST` kezelése, felmerülő problémák:
	* Refresh
	* Back gomb használata
	* Könyvjelző
* Redirect after post tervezési minta

---

## HTML formátum

* HyperText Markup Language
* W3C szabvány
* Szöveges formátum
* Szöveges tartalom reprezentálására
* Struktúra és tartalom (hisztorikusan megjelenés is)
* Hiperhivatkozások
* Fej, törzs
* Fa hierarchia
* Tagek

---

## HTML karakterkódolás

* HTML5-ben az alapértelmezett karakterkódolás az `UTF-8`

---

## Egyszerű HTML dokumentum

```html
<!DOCTYPE html>
<html>
    <head>
    	<title>Example</title>
    </head>
    <body>
    	<h1>Example Page</h1>
    	<p>This is an example page.</p>
    </body>
</html>
```

---

## DOM ábrázolás

![DOM](images/dom.jpg)

---

## CSS

* Cascading Style Sheets
* W3C szabvány
* Színek, méretek, elhelyezkedések, betűtípusok
* Elválik a tartalom és a forma
* Könnyebben változtatható a megjelenés
* Szelektorokkal kiválaszható elemeknek adható meg formátum
* Megadható a HTML-be ágyazva, fejlécben és külön állományban is

---

## CSS példa

```html
<h1>A CSS használata</h1>
```

```css
h1 {
    text-align: center;
    color: red;
    font-size: large;
    font-family: "Times New Roman", serif;
    font-style: italic;
}
```

---

## Beágyazott CSS

```html
<h1 style="color: red;">A CSS használata</h1>
```

---

## CSS a fejlécben

```html
<html>
	<head>
		<style>
			h1 {
				color: red;
			}
		</style>
	</head>
	<body>
		<h1>A CSS használata</h1>
	</body>
</html>
```

---

## Hivatkozás külső CSS állományra

```html
<html>
	<head>
		<link rel="stylesheet" href="styles.css" />
	</head>
	<body>
		<h1>A CSS használata</h1>
	</body>
</html>
```

---

## Rich Internet Application (RIA)

* Böngésző a kliens
* Operációs rendszert kihasználó alkalmazásokkal majdnem megegyező funkcionalitást képes nyújtani
* Böngésző technológiák fejlődése tette lehetővé
* Első implementációk: Google várható kifejezések, Google Maps, GMail
* HTML, CSS, JavaScript megoldások
* Adobe Flash, Microsoft Silverlight eltűnőben, JavaFX még nem terjedt el
	* Külön telepítés szükséges, nem a böngészőben beágyazva fut, csak onnan indítható
* Biztonsági vonzatok (homokozó)

---

## Alkalmazás architektúrája

* Gyakori, hogy az üzleti logika, és a felhasználó felület külön
technológiával kerül megvalósításra
* Alkalmazás két részre bontása:
	*	Backend: perzisztencia, üzleti logika
	* Frontend: felhasználói felület

---

## JavaScript

* Programozási nyelv
* Böngészők tudják értelmezni és futtatni
* Manapság böngészőn kívül is kezd terjedni, általános célú nyelvvé válhat
* Független a Java programozási nyelvtől

---

## HTML oldalba ágyazott JavaScript kód

```html
<input type="button" onclick="alert('Hello World!');" value="Click me!" />
```

---

## HTML oldal fejlécébe ágyazott JavaScript kód

```html
<head>
	<script type="text/javascript">
		onload = function() {
			document.getElementById('mybutton').addEventListener('click', 
				function(e) {
						alert('Hello World!');
					});
		}
	</script>
</head>
```

---

## JavaScript külön állományban - html

```html
<!DOCTYPE html>
<html>
<head>
	<script src="myscript.js" type="text/javascript"></script>
</head>
<body>
	<input id="mybutton" type="button" value="Click me!" />
</body
</html>
```

---

## JavaScript külön állományban - js

A `myscript.js` állomány tartalma:

```javascript
onload = function() {
	document
		.getElementById('mybutton')
		.addEventListener('click',
			function(e) {
				alert('Hello World!');
			});
}
```

---

class: inverse, center, middle

# Felületi tesztelés Seleniummal

---

## Selenium

* Böngésző automatizálás, tipikusan webes alkalmazások tesztelésére
* Eszközkészlet, több eszközből áll


![Selenium logo](images/selenium-logo.png)

---

## Selenium tulajdonságai

* Platformfüggetlen (Windows, Apple OS X, Linux, pl. Ubuntu)
* Képes meghajtani a különböző böngészőket is (Firefox, Internet Explorer, Safari, Opera, Chrome)
* Nyílt forráskódú, ingyenes

![Selenium logo](images/browsers_200.png)

---

## Felhasználási területek

* Funkcionális tesztelés
* GUI tesztelés
* Regressziós tesztelés
* Böngészőfüggetlenség tesztelése

![Selenium felhasználási területek](images/usage_200x.png)

---

## Selenium helye a tesztpiramisban

* E2E tesztelés
* GUI oldalról
* E2E tesztelés erőforrásigényes teszt készítés és teszt futtatás szempontjából is
    * Rendszer tesztelése a környezetével integrálva
    * Környezet megfelelő állapotban van?
    * Böngészők, virtuális ablakozó rendszer
    * Lassú
* Ne függj törékeny, gyakran változó dolgoktól, mint a GUI
    * Fragile Test Problem - változik a GUI, változtatni kell a teszteseteket

---

## Selenium alkalmazási területei

* Ha kevés teljes folyamaton átívelő, több lépésből álló E2E
tesztem van, ami a core üzleti funkcionalitást teszteli (happy path), (sanity)
* Megkérdőjelezhetőek a klasszikus alapelvek:
    * Egy teszt egy dolgot tesztel, egy dologra ellenőrzök
        * Több lépés esetén több ellenőrzés
* Ha nem törik el: jön a pénz
* Ha eltörik: nem jön a pénz

---

## Eszközök

* Selenium IDE: felvétel és visszajátszás grafikus felületen
* Selenium WebDriver: böngészővezérlés (pl. programozási nyelvekből API-n keresztül)
* Selenium Grid: automatizált tesztelés több gépről, összehangoltan

![Selenium tools](images/tools_400x.png)

---

## Selenium IDE

* Felvétel és visszajátszás (tesztesetek lépésekkel)
* Chrome vagy FireFox Add-On
* Programozási nyelv funkciók: parancskészlet, paraméterezés, változók, vezérlési elemek
* IDE funkciók, pl. projektkezelés, autocomplete, debug
* Parancssori futtatási lehetőség

---

## Selenium telepítése (gyakorlat)

* https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/
* https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd

---

## Selenium IDE indítása

* Új projekt létrehozása, és felvétel
* Létező projekt megnyitása
* Új projekt létrehozása
* Selenium IDE bezárása

---

##  Welcome screen

![Welcome screen](images/welcome_600x.png)

---

## Első teszt felvétele és visszajátszása (gyakorlat)

* http://host/locations/server
* Új lokáció felvétele helyes adatokkal
* Eredmény ellenőrzése: Jobb klikk/Selenium IDE/Assert text (`Location has saved.`)

---

## Selenium IDE képernyő

![Selenium IDE](images/selenium-ide_500x.png)

---

## Futtatás

* Base URL
* Run all tests
* Run current test
* Execution speed
* Log ablak

---

## Debug

* Breakpoints (Toggle breakpoint - `B`)
* Disable all breakpoints
* Stop test execution
* Resume test execution
* Play to this point
* Play from here

---

## Fájlkezelés

* Project név
* Create new project
* Open project
* Save project

---

## Tesztek szervezése

* Tests (test cases)
  * Rename, Duplicate, Delete, Export
* Test suites
  * Add tests, Rename, Delete, Settings, Export
* Executing

---

## Új teszt felvétele (gyakorlat)

* http://host/locations/server
* Új lokáció felvétele helytelen adatokkal
* Eredmény ellenőrzése: Jobb klikk/Selenium IDE/Assert text (`Location has saved.`)

---

## Teszt lépések

* Navigator
    * Command (Enable/Disable, Add new window configuration)
    * Target
    * Value
    * Description

---

## Gyakori parancsok

* `open`
* `type`
* `click`
* assert, pl. `assert title`, `assert text` - ha hamis, leáll a futás
* verify, pl. `verify title`, `verify text` - ha hamis, warning
* https://www.seleniumhq.org/selenium-ide/docs/en/api/commands/
* Reference ablak

---

## Lépések szerkesztése

* Cut, Copy, Paste, Delete
* Sorrendezés drag n' droppal
* Insert new command
* Clear all command
* Record from here

---

## Komponensek kijelölése

* Formátuma: `locatorType=location`
* https://www.guru99.com/locators-in-selenium-ide.html
* Id alapján
* Name alapján (filterelhető)
* Link
* CSS
    * Developer tools/Inspector/Copy CSS selector
* XPath
    * Developer tools/Inspector/Copy XPath

---

## Locator Selenium IDE támogatás

* Selenium IDE: Select target in page, Find target in page
* Egyszerre több locatort is megjegyez, amelyik sikerül
    * Amennyiben további fejlesztés miatt az egyik locator nem ad eredményt, a másik még adhat
---

## CSS selector

* `id` attribútum alapján: `css=tag#id`, pl. `css=input#name-input`
* CSS class alapján: `css=tag.class`, pl. `css=input.btn`, vagy tag nélkül `.btn`
* Attribútum érték alapján `css=tag[attribute=value]`, pl. `css=input[type=submit]`

---

## XPath

* W3C szabvány
* Egy XML dokumentum elemei és attribútumai közötti navigációt biztosítja
* XPath szintaktika segítségével definiálhatjuk az XML dokumentum részeit
* Kifejezések segítségével mozoghatunk az XML dokumentumban
* https://codebeautify.org/Xpath-Tester

---

## XPath példák

* `/html`
* `/html/body`
* `//input`
* `/html/@lang`

---

## XPath predicates 1.

* `/html/table/tbody/tr[1]` - első `tr`
* `/html/table/tbody/tr[last()]`  - utolsó `tr`
* `/html/table/tbody/tr[last() - 1]`  - utolsó előtti `tr`
* `/html/table/tbody/tr[position() < 3]` - első két `tr`

---

## XPath predicates 2.

* `//input[@id]` - van `id` attribútuma
* `//input[@id="name-input"]` - `id` attribútumának értéke `name-input`

---

## XPath ismeretlen csomópontok

* `/html/body/*` - összes gyerek
* `//*` - összes elem
* `//*[@id="name-input"]` - összes tag, megadott attribútummal

---

## Új assert (gyakorlat)

* A táblázatban megjelenik-e <span style="color:white">xpath=//td[contains(text(), 'Győr')]</span>
* A táblázatban ha megjelenik, a koordináta <span style="color:white">xpath=//tr[td[contains(text(), 'Győr')]]/td[2]</span>

---

## Legjobb gyakorlatok

* Körültekintően nevezzük el a teszteket
* Selectornál támaszkodjunk az `id` értékekre, fejlesztők támogatása szükséges
  * `id` elnevezés legyen konzekvens (elnevezési konvenció)
* Idempotens és izolált
* Tesztesetek legyenek egyszerűek
* DRY - don't repeat yourself
* Használjuk Continuous Integration rendszeren belül

---

## Idempotencia és izoláltság

* Tesztesetek egymásra hatással vannak
    * Állapot: pl. adatbázis
* Ugyanazon tesztkörnyezeten több tesztelő vagy harness dolgozik
* Megoldás:
    * Teszteset "rendet tesz" maga előtt, un. set-up
    * "Rendet tesz" maga után, un. tear down
    * Test fixture
        * Legszélsőségesebb megoldás: adatbázistörlés


---

## Változók használata

* `store [érték] [változónév]`
* `echo [érték]` parancs, változóra: `${változónév}`

---

## Változó újrafelhasználása (gyakorlat)

* A név értéke legyen a `name` változóban

---

## JavaScript + változó (gyakorlat)

* `execute script | return Date.now(); | now`
* Névben legyen benne ez a generált szám

```javascript
confirm("Hello World!");console.log("Hello Console!");
```

---

## XPath kifejezés értéke változóba (gyakorlat)

* Id visszaolvasása
* `store text` <span style="color:white">xpath=//tr[td[contains(text(), 'Győr')]]/td[1]</span>

---

## Másik teszteset futtatása

* `run` parancs

---

## DRY megszüntetése (gyakorlat)

* `Answer questions` hívása `run` parancs segítségével

---

## Control flow

* Elágazás és ciklus
* https://www.seleniumhq.org/selenium-ide/docs/en/introduction/control-flow/

---

## Ciklus (gyakorlat)

* Módosítsd úgy a `Answer questions` teszt esetet, hogy kétszer válassza ki az első választ!
* Tipp: módosítsd úgy a locatort (XPath-ra), hogy mindig az első gombra klikkeljen

---

## Command-line Runner

* Node.js (https://nodejs.org/en/download/)
* `selenium-side-runner`: `npm install -g selenium-side-runner`
* `geckodriver`: `npm install -g geckodriver`

(Windowson letöltendő és PATH-ba helyezendő: https://github.com/mozilla/geckodriver/releases)

Futtatás

* `selenium-side-runner -c "browserName=firefox" testapp.side`

---

## Selenium WebDriver

* Böngészővezérlés programozottan
* Különböző programozási nyelvekhez illesztés: C#, Groovy, Java, Perl, PHP, Python, Ruby and Scala
* Driver böngészőnként (Firefoxhoz geckodriver, https://github.com/mozilla/geckodriver)

---

## WebDriver

![WebDriver](images/webdriver_500x.png)

---

## Selenium Javaval

* Selenium IDE képes exportálni

---

## Selenium Pythonnal

* https://selenium-python.readthedocs.io/

---

## Új projekt

* `requirements.txt` állományba `selenium`
    * Install requirements
* Új könyvtár létrehozása
    * `.py` Ptyhon állományok létrehozása

---

## Első teszteset

```python
from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\Java\geckodriver-v0.20.1-win64\geckodriver.exe")
driver.get("http://localhost:8080/")
assert "Test Application" in driver.title

# driver.close()
```

---

## Input

```python
nameInput = driver.find_element_by_id("txtUserName")
nameInput.clear()
nameInput.send_keys("vicziani")

button = driver.find_element_by_xpath("/html/body/form/button")
button.click()
```

---

## Elem szövegének vizsgálata

```python
secondAnswerLabel = driver.find_element_by_xpath("/html/body/form/label[2]")
print (secondAnswerLabel.text)
assert "1b válasz" in secondAnswerLabel.text
```

---

## Újrafelhasználás, page object

---

## Adatvezérelt tesztelés

---

## Ismétlő kérdések

* Milyen komponensekből áll a Selenium? Melyiknek mi a feladata?
* Mi a Selenium fő célja?
* Milyen területeken használható a Selenium?
* Mire való a Selenium IDE?
* Milyen szoftverként jelenik meg, hogy kell telepíteni?
* Hogyan lehet a legegyszerűbben egy tesztet elkészíteni?
* Milyen debugging lehetőségek vannak benne?
* Milyen gyakori tesztlépések vannak?
* Mi az a lokátor? Hogyan lehet megadni?

---

## Ismétlő kérdések 2.

* Mik a teszteléssel kapcsolatos legjobb gyakorlatok?
* Hogy lehet a kódismétlést minimalizálni?
* Hogyan lehet változót deklarálni és használni?
* Milyen vezérlési szerkezetek vannak?
* Hogyan lehet parancssorban futtatni teszteseteket?
* Mire való a WebDriver?
* Milyen programozási nyelveket támogat?
* Milyen lépéseket ismersz?
* Milyen tervezési mintát ismersz?
