# Selenium IDE feladatok 3.

## Háromszögek (kedvenc!)

Olyan programot fogunk írni, és tesztelni, mely három beírt szám alapján
eldönti, hogy lehet-e az oldalhosszakkal háromszöget rajzolni, és ha lehet,
milyet.

Készíts egy HTML oldalt `triangles.html` néven, melyen van egy cím, kis szöveg,
és három beviteli mező, amiben a háromszög oldalait lehet megadni!
A mező azonosítók rendre legyenek `a-input`, `b-input`, `c-input`. A
mezők egymás alatt jelenjenek meg. Mindegyiknek legyen egy címkéje!
(Járj utána hogy kell használni a `<label>` taget!)

Mindegyik beviteli mezőnek egy pixel széles kerete legyen, és mikor a felhasználó
ráklikkel, akkor változzon a színe és a vastagsága! (CSS, keresés Google-lel!)

Legyen egy gomb, számol felirattal, `calculate-button` id-val! Fontos az id-k
pontossága, ugyanis az alant megadott JavaScript ezeket fogja használni.

A gomb alatt legyen egy üres lista, `<ul>` taget használj, mely megjeleníti az eredményt, ennek
az azonosítója `result-ul` legyen.

Ha bekötöd az alul megadott JavaScriptet, működni fog az alkalmazás. (Van benne egy számolási hiba, találd meg!)

Írj egy programot, ami leteszteli a program működését `test-triangle.py`! Egy programon belül
próbálj ki több esetet! A teszt írja be a megfelelő számokat, majd ellenőrizze, hogy 
a program jól működik-e! (White box testing!) Vigyázz, a program nem lecseréli az üzenetet,
hanem mindig a listába beszúrja, ezért xpath-szal az utolsó elemet kell lekérdezned! (Google vagy a mentor segít!)

Vigyázz, a programodban ne legyen kódismétlés! Azaz ne így nézzen ki!

```python
driver.find_element(By.ID, "a-input").send_keys("12");

driver.find_element(By.ID, "a-input").send_keys("17");

driver.find_element(By.ID, "a-input").send_keys("21");
```

Hanem a program elején kérdezd le a négy komponenst egy változóba, és utána ezekre hivatkozz.

```python
a_input = driver.find_element(By.ID, "a-input");

a_input.send_keys();
```

A végén az egészről készíts egy képernyőképet!


```javascript
function classify(a, b, c) {
        if (isNaN(a)) {
            return "Első nem szám";
        }
        a = parseInt(a);

        if (isNaN(b)) {
            return "Második nem szám";
        }
        b = parseInt(b);

        if (isNaN(c)) {
            return "Harmadik nem szám";
        }
        c = parseInt(c);

        if (a <= 0 || b <= 0 || c <= 0) return "Negatív";
        if (a == b && b == c) return "Egyenlő oldalú";
        if (a >= b+c || c >= b+a || b >= a+c) return "Nem háromszög";
        if (b==c || a==b || b==c) return "Egyenlő oldalú";
        return "Általános";
}

window.onload = function() {
    document.getElementById("calculate-button").onclick = function() {
        let a = document.getElementById("a-input").value;
        let b = document.getElementById("b-input").value;
        let c = document.getElementById("c-input").value;

        let result = document.getElementById("result-ul");

        result.innerHTML += "<li>" + "a = " + a + ", b = " + b + ", c = " + c + ": " + classify(a, b, c) + "</li>";
    }
};
```

## Státuszkódok kutyusokkal

Írj egy programot `httpstatus.py` néven, mely a felhasználótól konzolról bekér egy státuszkódot,
és kiírja annak megnevezését, valamint készít egy képet a kódhoz tartozó kutyusról!

A program az elején `input()` függvénnyel kérje be a státuszkódot, 
menjen el a https://httpstatuses.com/ oldalra, és keresse ki a státuszkódot, majd 
menjen a https://httpstatusdogs.com/ oldalra, és készítsen a megfelelő kutyusról egy
screenshotot.

Mindkét oldalon állítson össze
egy XPath lekérdezést, ami kikeresi a megfelelő elemet a DOM-ban.

Az XPath összeállítására egy példa:

```python
id = input('Add meg a lokáció azonosítóját!')
xpath = "//tr[td[text() =='" + id + "']]/td[2]"
print(xpath)
name_td = driver.find_element(By.XPATH, xpath)
```

A kódrészlet bekér egy azonosítót, legyen ez pl. `12`. A második sor ebből összeállítja
a következő xpath-t: `//tr[td[text() == '12']]/td[2]`. Figyeld meg, hogy milyen
trükkösen van megoldva az aposztrófok kezelése. A Pythonban idézőjelekkel határoltam a szöveget,
hogy elhelyezhessek benne szimpla idézőjelet.
A harmadik sor kiírja az xpath kifejezést, hogy ellenőrizni lehessen.

A https://httpstatuses.com/ oldalon `<li>`-ket kell keresni.

A https://httpstatusdogs.com/ oldalon `<div>`-et kell keresni, és arról készíteni egy státuszkódot.

## Fahrenheit Celsius váltás

Írj egy programot `fcconverter.py` néven, mely bekér egy számot, ez a hőmérséklet Celsiusban,
majd átváltja Fahrenheitba.

Nem kell az algoritmust Pythonban leprogramozni (azt majd később!), hanem a program menjen el
a https://www.convertworld.com/hu/homerseklet/fahrenheit.html oldalra, írja be a számot,
és keresse ki az eredményt, és írja ki a konzolra (`print`)!