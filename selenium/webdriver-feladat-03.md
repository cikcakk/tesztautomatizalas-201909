# AJAX feladatok

Telepítettem a http://www.learnwebservices.com/locations/
címre az unalomig ismert Locations alkalmazás AJAX-os verzióját.

Nézd meg, hogy amíg az alkalmazást teszteled, történik-e oldalváltás!
Próbáld ki az új felvitelt, módosítást, törlést, és nézd meg, hogy a 
háttérben milyen HTTP kérések vannak.

Írj egy olyan függvényt, mely felveszi egy új helyet a
paraméterként megadott névvel és koordinátákkal!

Majd írj egy függvényt, ami bevárja, hogy a
_Location has created_ üzenet megjelenjen!

Majd írj egy függvényt, ami bevárja, hogy a megfelelő
nevű hely megjelenjen a táblázatban!

Amennyiben túl sok van, az sem baj, mert paraméterezni lehet,
hogy mennyi jelenjen meg egyszerre. A következő címet kell ekkor használni: http://www.learnwebservices.com/locations/?size=100

Így nem kell a lapozással foglalkozni, hiszen egyszerre száz fog 
megjelenni.

Majd írj egy függvényt, ami meghívja az előző két függvényt, ezzel
tesztelve a felvételt! Legyen a névben timestamp!

Írj egy függvényt, mely az adott nevű helyet módosítja! (A módosítottban
  is legyen timestamp.)
Írj egy függvényt, amely bevárja a _Location has modified_ üzenetet! 

Most két olyan függvényed van, ami bevár egy üzenetet. Írj helyette egyet,
melynek át kell adni az üzenet szövegét!

Írj egy függvényt, mely a módosítás tesztesete! Ez létrehoz egyet
az egyik függvénnyel, majd módosítja a másikkal, majd bevárja 
a _Location has modified_ üzenetet a harmadik függvénnyel, és az utolsó
függvénnyel bevárja, hogy a megfelelő nevű hely megjelenjen a táblázatban!
Itt már a létező függvényekből kell építkezned.

Írj egy függvényt, ami a hibaüzenetet teszteli! Hívd meg a létrehozó
függvényt üres névvel, majd várj a megfelelő hibaüzenetre!

Írj egy függvényt, mely a paraméterként megadott nevű helyet törli! (Kattintson rá a confirmation dialogra!)

Így kell WebDriverben ráklikkelni a confirmation dialogra:

```python
driver.switch_to.alert.accept()
```

Írj egy függvényt, mely arra vár, hogy a megadott nevű hely eltűnjön a táblázatból.
Az eltűnést úgy kell implementálni, hogy a megjelenés ellenkezőjére vársz használva
az `until_not` függvényt.

```python
WebDriverWait(driver, 10).until_not(
  expected_conditions.presence_of_element_located((By.XPATH, xpath))
)
```

Írj egy függvényt, mely a törlést teszteli! Először felvesz egyet,
majd törli, majd bevárja a sikeres törlés üzenetetét, és azt, hogy a
hely eltűnjön a táblázatból.