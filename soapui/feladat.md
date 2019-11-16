# SOAP webszolgáltatások és SoapUI gyakorlati feladatok

## Celsius to Fahrenheit converter

A http://www.learnwebservices.com/ oldalon megtalálható egy webszolgáltatás,
mely képes celsius és fahernheit között váltani.
A WSDL dokumentuma megtalálható a http://www.learnwebservices.com/services/tempconverter?wsdl címen.

Térképezd fel, hogy a webszolgáltatás hány operációt tartalmaz! Mindegyik operációra írj legalább egy
tesztesetet! Próbálkozz boundary-value analysis-szel is!

## Locations alkalmazás

A http://www.learnwebservices.com/locations/ címen megtalálható egy kedvenc
helyeket nyilvántartó alkalmazás. Ez nyújt SOAP webszolgáltatás API-t,
mely WSDL dokumentuma megtalálható a http://www.learnwebservices.com/locations/services/locations?wsdl
címen.

Ez tipikusan megvalósítja a CRUD műveleteket, írj mind a négy művelethez (listázás, létrehozás,
módosítás, törlés) teszteseteket! Gondolj azokra az ágakra is, amikor helytelen adatot adunk meg!
(Pl. üres, túl kicsi vagy túl nagy szám.)
Egy lépésből álló tesztesetek esetén csak a létrehozáshoz tudunk korrekt tesztesetet létrehozni,
hiszen a listázáshoz előfeltétel, hogy az alkalmazás egy adott állapotban legyen. Ugyanígy
a módosításnál és a törlésnél is léteznie kell azzal az azonosítóval, ami alapján módosítani vagy
törölni akarunk.

Tervezz meg a listázásra, módosításra és törlésre is több lépésből álló teszteseteket
(csak írd le). Láttuk, hogy a Postman esetén az egyik kérésből kellett adatot átvinni a másik
kérésbe. Írd le szövegesen, hogy honnan kell adatot kiolvasni, és hová kell beilleszteni.
(Emlékezz vissza, Postman esetén a JSON válaszból kellett kiolvasni az azonosítót, és 
át kellett vinni a következő kérés URL-jébe!)

Példa a következő egy másik fiktív banki rendszer esetén, ami egy átutalást tesztelne.
Létrehozunk két számlát, az elsőre utalunk 200 egységet, majd az elsőről átutalunk 50 egységet a másodikra.
Azt kell ellenőrizni, hogy a számlákat listázva az elsőn 150, a másodikon 50 egység lesz.

```
Teszt lépések:

Meg kell hívni a "createAccount" operációt, aminek hatására a válaszban a <account-number> tagen belül
megjelenik a létrehozott bankszámlaszám (legyen ez a no1)
Meg kell hívni a "createAccount" operációt még egyszer, aminek hatására a válaszban a <account-number> 
tagen belül megjelenik a létrehozott bankszámlaszám (legyen ez a no2)
Meg kell hívni a "deposit" operációt, aminek az <dest-account-number> tagjében meg kell adni a no1 számot,
valamint legyen az összeg 200 egység

Elvárt eredmény:

Meg kell hívni a "transfer" operációt, aminek az <src-account-number> tagjében meg kell adni a no1 számot,
a <dest-account-number> tagjében meg kell adni a no2 számot, és a <amount> tagben meg kell adni 50-et
Meg kell hívni a "listAccounts" operációt, az eredményből ki kell választani azt a <account> taget,
melyben van egy gyermek <account-number> tag, aminek értéke a no1, és a <balance> tagben 150-nek kell 
szerepelnie.
Ahol az <account-number> tag értéke no2, ott a <balance> tag értéke 50 legyen
```

