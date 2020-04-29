# Asennusohje

## Sovelluksen käyttö paikallisesti

Voit asentaa sovelluksen omalle koneellesi. Tätä varten sinulla tulee olla käytössäsi Pythonin versio 3.5 tai uudempi. Käytössäsi tulee olla myös [PostgreSQL](https://www.postgresql.org/)-tietokannanhallintajärjestelmä. 

Aja ensin seuraava komento haluamassasi hakemistossa projektin lähdekoodin lataamiseksi koneellesi:
```
git clone https://github.com/sinisaarinen/KielikoulunKurssitarjonta.git
```
Sovelluksen lähdekoodia voi nyt tarkastella hakemistossa `KielikoulunKurssitarjonta`.

Seuraavaksi luodaan virtuaaliympäristö. Tämä onnistuu ajamalla projektin juuressa seuraavan komennon:
```
python3 -m venv venv
```
Virtuaaliympäristö löytyy nyt hakemistosta `venv` ja se voidaan ottaa käyttöön suorittamalla:
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
Sovelluksen voi avata nyt selaimessa. Jos sovellus on käynnissä portissa 5000, sovellus avautuu selaimella osoitteessa `localhost:5000`.

## Sovelluksen käyttö Herokussa

Voit käyttää sovellusta myös Herokussa. Tällöin sinun tulee luoda tunnukset [Herokuun](https://dashboard.heroku.com/login). Lisäksi tarvitset käyttöösi [Git-versionhallinnan](https://git-scm.com/downloads).

Lataa seuraavaksi käyttöösi Herokun [komentorivityövälineet](https://devcenter.heroku.com/articles/heroku-cli).

Nyt voit luoda projektin komennolla
```heroku create <projektin_nimi>```

Lisää tämän jälkeen Herokun etärepositorio paikalliseen versionhallintaan komennolla
```git remote add heroku https://git.heroku.com/<projektin_nimi>.git```

Määritä Herokuun ympäristömuuttuja komennolla
```heroku config:set HEROKU=1```

ja lisää sovellukselle tietokanta komennolla
```heroku addons:add heroku-postgresql:hobby-dev```

Voit pushata projektin Herokuun komennolla
```git push heroku master```
