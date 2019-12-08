# Selenium WebDriver gyakorlás - 7. óra

## Alkalmazás telepítése

Az alkalmazást érdemes mindenkinek a saját gépén futtatnia, hiszen így nem
keverednek össze a tesztadatok. 

Az alkalmazás futtatáshoz a saját gépre
telepített MariaDB adatbáziskezelő szükséges. Elegendő egy üres séma `locations` néven, valamint egy `locations` felhasználó `locations` jelszóval. (HeidiSQL felületen létrehozható és felvehető.)

A futtatható alkalmazás letölthető a https://raw.githubusercontent.com/vicziani/tesztautomatizalas-201909/master/selenium/locations-app.jar címről.

Az alkalmazás futtatásához Java 13 szükséges, mely letölthető a https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html címről (`jdk-13.0.1_windows-x64_bin.exe`). A feltelepítés után a következő paranccsal indítható, Windows
parancssorból, abból a könyvtárból, melyben a letöltött `jar` állomány van:

```
"C:\Program Files\Java\jdk-13.0.1\bin\java.exe" -jar locations-app.jar
```

A konzolon a `LocationsApplication` szövegnek kell megjelennie. Ezután az alkalmazás elérhető a `http://localhost:8080` címen.

Előfordulhat, hogy a `8080`-as portot már használja valamilyen szoftver. Ekkor ez az üzenet
jelenik meg:

```
Web server failed to start. Port 8081 was already in use.
```

Ekkor helyezzetek el
a `jar` fájl mellett egy `application.properties` állományt a következő tartalommal:

```
server.port=8081
```

Ekkor a `8081`-es porton fog elindulni, és ezt használjátok a böngészőben is.


## Kiindulás

Indulj ki a `locations_operations.py` állományból!
Ez keverve tartalmaz függvényeket a következőkre:

* Különböző oldalakhoz tartozó függvények
* Navigálás
* Űrlap kitöltés
* Klikkelés linkre, gombra
* Megjelenő szövegek ellenőrzése

## Literal string interpolation

Python 3.6 óta lehetséges un. literal string interpolation, azaz
stringben lehet változóneveket használni. Ehhez a string előtt
az `f` karaktert kell megadni. Példa:

```python
# Régi megoldás
xpath = "//tr[td[text() = 'name']]/td[2]".replace("name", name)

# Új megoldás
xpath = f"//tr[td[text() = '{name}']]/td[2]"
```

## Default values

* A `fill_create_location_form()` függvényt módosítsd úgy, hogyha
nem adunk meg paramétert, az értékek `Budapest` és `47.497912,19.040235`
értékak legyenek!


## Adatbáziskezelés

Ahhoz, hogy a tesztesetek lefussanak, az adatbázist mindig
üres állapotba kell hozni.

Ahhoz, hogy Pythonból adatbázist tudjunk kezelni, szükség van
az adott adatbázis connectorra, ehhez egészítsük ki a
`requirements.txt` állományt a következővel:

```
mysql-connector
```

Majd kattintsunk az _Install requrement_ feliratra.

Lekérdezés:

```python
from mysql.connector import connect

conn = connect(
    host="localhost",
    user="locations",
    passwd="locations",
    database="locations"
)

cursor = conn.cursor()
cursor.execute("select name, lat, lon from locations")
for (name, lat, lon) in cursor:
    print(f"{name} ({lat}, {lon})")
cursor.close()
```

Feltétellel:

```python
cursor.execute("select lat, lon from locations where name = %s", (name, ))
```

Módosítás:

```python
cursor.execute("delete from locations")
conn.commit()
```

### Feladatok

* Minden teszteset futtatása előtt töröld ki az adatbázist! Írj hozzá egy `delete_locations()` függvényt!
* Írj egy `count_locations()` függvényt, mely visszaadja, hogy hány rekord van
a `locations` táblában!
* Írj egy `print_locations()` függvényt, mely kiírja az összes `locations` rekordot!
* Írj egy `insert_location(name, coords)` függvényt, mely
beszúr egy új `locations` rekordot a megadott paraméterekkel!
* Írj egy `assert_location_exists(name, coords)` függvényt, mely
ellenőrzi, hogy a paraméterként `locations` rekord szerepel-e az
adatbázisban!

## Page object

A `pages/google_page.py` fájlba.

```python
class GooglePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.google.com/")

    def type_search_term(self, term):
        self.driver.find_element_by_name("q").send_keys(term)
```

A `google_operations.py` fájlba.

## Pytest

```python
class TestCalculator():
    def setup_method(self):
        self.operand1 = 5
        self.operand2 = 10

    def test_true(self):
        assert 15 == self.operand1 + self.operand2
```