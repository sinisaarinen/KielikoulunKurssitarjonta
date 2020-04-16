# Asennusohje

Voit asentaa sovelluksen omalle koneellesi. Tätä varten sinulla tulee olla käytössäsi Pythonin versio 3.5 tai uudempi. Käytössäsi tulee olla myös [PostgreSQL](https://www.postgresql.org/)-tietokannanhallintajärjestelmä. 

Aja ensin seuraava komento haluamassasi hakemistossa projektin lähdekoodin lataamiseksi koneellesi:
```
git clone https://github.com/sinisaarinen/KielikoulunKurssitarjonta.git
```
Sovelluksen lähdekoodia voi nyt tarkastella hakemistossa KielikoulunKurssitarjonta.

Seuraavaksi luodaan virtuaaliympäristö. Tämä onnistuu ajamalla projektin juuressa seuraavan komennon:
```
python3 -m venv venv
```
Virtuaaliympäristö löytyy nyt hakemistosta venv ja se voidaan ottaa käyttöön suorittamalla:
```
source venv/bin/activate
```

Aja tämän jälkeen seuraava komento hakemiston juuresta asentaaksesi riippuvuudet:
```
pip install -r requirements.txt
```

Tämän jälkeen voit käynnistää sovelluksen ajamalla hakemiston juuresta seuraavan komennon:
```
python run.py
```
Sovelluksen voi avata nyt selaimessa. Jos sovellus on käynnissä portissa 5000, sovellus avautuu selaimella osoitteessa localhost:5000.
