# Adatbáziskezelés Pythonból - Gyakorlati feladatok

## Környezet előkészítése

A gyakorlati feladatok a PetClinic projekt adatbázisát használják.
Ennek előkészítéséhez a következő lépéseket kell megtenni.
Ezek HeidiSQL-ben elvégezhetőek.

* Új séma létrehozása: `petclinic`
* Új felhasználó és jelszó létrehozása: `petclinic` / `petclinic`
* Felhasználónak jogosultságot kell biztosítani a `petclinic` sémához
* Táblákat létrehozó szkript futtatása: https://github.com/spring-projects/spring-petclinic/blob/master/src/main/resources/db/mysql/schema.sql
* Adatokat beillesző szkript futtatása: https://github.com/spring-projects/spring-petclinic/blob/master/src/main/resources/db/mysql/data.sql

Amennyiben a feladatok során az adatbázis megsérülne, adatok módosulnának, mindig újra lehet kezdeni úgy, hogy
el kell dobni az összes táblát, majd újra lefuttatni a szkripteket.

Az összes tábla törléséhez válasszuk ki a sémát, és _jobb oldalon_ fognak megjelenni a táblák. Itt jelöljük ki az összeset
_Shift_ billentyűvel, majd _Jobb klikk / Eldobás..._ menüpontot nyomjuk meg. Vigyázat, a bal oldalon ezt nem lehet megtenni.

## Feladatok

A megírt SQL utasításokat érdemes először HeidiSQL-ben kipróbálni, és csak utána futtatni Pythonból.

* Írj egy `print_owner_names()` függvényt, mely kiírja a konzolra a gazdik neveit (kereszt és vezetéknév)!
* Írj egy `list_owner_names()` függvényt, mely egy listába összegyűjti a gazdik neveit, és visszaadja ezeket (kereszt és vezetéknév)!

A listába összegyűjteni elemeket a következőképp lehet:

```python
names = []

for i in range(0, 10):
    names.append(f"John Doe {i}")
print(names)
```

* Írj egy `list_owner_names_who_lives_in(city)` függvényt, mely azon gazdik neveit adja vissza, akik a paraméterként
megadott városban laknak!
* Írj egy `find_owner_by_id(id)` függvényt, ami egy gazdi adatait adja vissza azonosító alapján egy dictionary-ban!

Ne feledd, dictionary létrehozása így történhet:

```python
owner = {"name": "George Franklin", "address": "110 W. Liberty St.", "city": "Madison", "telephone": "6085551023"}
```

* Írj egy `count_owners_who_lives_in(city)` függvényt, amely visszaadja, hogy hány gazdi él a megadott városban!
* Írj egy `create_owner_with(name, address, address, city, telephone)` függvényt, ami beszúr egy gazdit! Vigyázz, a nevet
szét kell bontani!
* Írj egy `create_owner(owner)` függvényt, mely a fentebb megadott dictionary-t várja paraméterül, és ezekkel az adatokkal
hozza létre!
* Írj egy `assert_owner_exists(name)` függvényt, mely azt ellenőrzi, hogy a paraméterként megadott nevű gazdi létezik!
* Írj egy `delete_owner_by_id(id)` függvényt, mely a paraméterként átadott azonosító alapján törli a gazdit!
* Írj egy `pet_names_younger_than(date)` függvényt, mely visszaadja a paraméternél később született kedvencek neveit!

## Bonyolultabbak

* Írj egy `get_owner_of(pet_name)` függvényt, mely visszaadja a paraméterként megadott állatka gazdijának nevét!
* Írj egy `add_owner_to(owner_name, pet_name, birth_date, type_name)` függvényt, mely felvesz egy új állatkát!
 Ez bonyolult, először le kell kérdezni a gazdi azonosítóját név alapjén, majd a típus azonosítóját a típus név (pl. `dog`)
 alapján, és beszúráskor ezt a két azonosítót kell használni!
* Írj egy `get_pets_of(owner_name)` függvényt, mely visszaadja a paraméterként megadott nevű gazdi kedvenceit!
* Írj egy `print_visits_of(pet_name)` függvényt, mely kiírja az adott kedvenc neve alapján, hogy mikor volt orvosnál, és
mi történt ott.
