# Postman gyakorlati feladat 2.

Adott a Crystal Ball alkalmazás, mely elérhető a `http://www.learnwebservices.com/crystalball` címen,
és dokumentációja pedig a [`postman-feladat.md`](postman-feladat.md) állományban.

## Feladatok

Használj adatvezérelt tesztelést, és hozz létre Postman használatával tíz jóslatot a kövekező formátumban:

`John Doe 2019-09-25-én a Zsámbék településen lesz.`

A `creator` mezőben a saját nevedet add meg!

A jóslatban változzon a név, a dátum és a település neve. Egy darab teszt esetet írj egy külön Postman
Collectionben, mely egy lépésből áll, mely felveszi a jóslatot, és vissza is ellenőrzi, hogy a
`message` tartalma megfelelően került-e elmentésre.

Futtasd le úgy ezt a tesztesetet, hogy az adatokat egy külső CSV állományból töltse le! Az
állományt a [Mockaroo](https://mockaroo.com/) oldalon generáltasd le, három mezőből álljon:
név, dátum, településnév.

Egy újabb Collectionben hozz létre egy kérést, mely lekérdezi az összes jóslatot. Ennek eredménye egy JSON
fájl. Bár nem tanultunk rá eszközt, keress megoldást arra, hogy csak a te nevedhez tartozó
id-kat gyűjtsd ki egy szöveges állományba, sortörésekkel elválasztva. Használhatsz programozási nyelvet,
valami online szolgáltatást, Linux/Windows shell szkripteket, online szolgáltatást, szövegszerkesztőt,
Excelt. (Tíz esetén még a copy-paste is működik, de próbálj automata megoldást találni!)
Ez egy olyan speciális CSV állomány lesz, melyben nem lesz vessző, hiszen csak egy oszlopot tartalmaz.

Írj egy harmadik Collectiont, melybe egy kérést hozz létre, mely letöröl egy jóslatot! Szintén
használj adatvezérelt tesztelést, futtasd ezt a tesztesetet úgy, hogy add meg neki az előbb előállt fájlt.
Ennek hatására az állományban megadott azonosítójú jóslatokat ki kell törölnie.