# Käyttöohje

Kun olet suorittanut sovelluksen asennuksen koneellesi dokumentaatiosta löytyvän [asennusohjeen](installation.md) mukaisesti tai olet avannut sovelluksen [Herokussa](https://tsoha-harjoitus.herokuapp.com/), voit siirtyä käyttämään sovellusta tämän dokumentin ohjeiden mukaisesti.

## Rekisteröityminen

Sovellukseen pääsee rekisteröitymään vasemmalta yläpalkista löytyvän `Sign up` -linkin kautta. Rekisteröitymiseen tarvitaan käyttäjän nimi, uniikki käyttäjätunnus ja salasana. Rooliksi tulee valita 'client'.

## Sisään- ja uloskirjautuminen

Kun olet rekisteröitynyt sovellukseen, pääset sisäänkirjautumaan oikealta yläpalkista löytyvän `Log in` -linkin kautta. Syötä avautuvassa näkymässä käyttäjätunnuksesi ja salasanasi ja paina `Login`-nappia. Jos haluat tarkastella sovellusta admin-tilassa, voit kirjautua sisään käyttäjätunnuksella "admin1" ja salasanalla "admin".

Uloskirjautuminen onnistuu vastaavasti oikean yläkulman `Logout`-linkkiä painamalla.

## Kurssien ja kurssipaikkakuntien tarkastelu

Kursseja pääsee tarkastelemaan yläpalkista löytyvän `List courses`-linkin kautta ja kurssipaikkakuntia vastaavasti `List locations`-linkistä. Kurssin tiedoissa mainitaan kurssin nimi, kurssikoodi, kieli, taso, paikkamäärä, sijainti ja kurssikuvaus. Lisäksi voi tarkastella, missä kursseissa ilmoittautuminen on avoinna. Kurssipaikkakuntien tiedoissa taas mainitaan sekä paikkakunta että tarkempi sijainti.

## Kurssien hakeminen

Kursseja voi hakea `List courses`-linkin kautta avautuvassa näkymässä. Kurssien hakeminen onnistuu kurssin nimen, kurssikoodin, kielen tai tason (beginner, intermediate tai advanced) perusteella. Valitse valikosta haluamasi hakukriteeri, kirjoita hakukenttään hakusana ja paina `Search`-nappia. Sivulle listataan kaikki hakuasi vastaavat kurssit.

## Kurssille ilmoittautuminen

Kurssille voi ilmoittautua client-rooliin rekisteröitynyt ja kirjautunut käyttäjä. Ilmoittautumaan pääsee klikkaamalla `List courses`-näkymästä haluamansa kurssin kohdalla `Register for the course`-nappia. Nappi on näkyvissä vain, jos kurssille ilmoittautuminen on auki. Kurssille rekisteröitymiseen tarvitaan koko nimi, puhelinnumero ja toimiva sähköpostiosoite.

## Ilmoittautumisen muokkaaminen ja poistaminen (ei toimi vielä)

Tästä lisää pian.

## Admin-ominaisuudet

Admin-tunnuksilla kirjautuneena käytössä on joukko tavalliselle käyttäjälle näkymättömiä toimintoja.

### Uuden kurssin tai sijainnin lisääminen

Uuden kurssin pääsee lisäämään yläpalkista löytyvästä `Add a new course`-linkistä. Täytä lomakkeeseen kurssin tiedot ja paina `Add a new course`. Kurssisi löytyy nyt `List courses`-linkistä avautuvasta listasta.

Uuden sijainnin voi lisätä yläpalkin `Add a location`-linkin kautta. Täytä lomakkeeseen kurssipaikkakunnan nimi ja tarkempi sijainti tai osoite ja paina `Add a new location`. Lisäämäsi sijainti löytyy nyt `List locations`-linkkiä painamalla avautuvasta näkymästä.

### Kurssin tai sijainnin poistaminen

Lisätyn kurssin voi poistaa `List courses`-näkymästä klikkaamalla kurssin oikealta puolelta löytyvää `Delete`-nappia. Lisätyn sijainnin voi puolestaan poistaa `List locations`- näkymästä `Delete location`-nappia painamalla.

### Kurssin tai sijainnin muokkaaminen

Kursseja pääsee muokkaamaan painamalla `List courses`-näkymässä `Edit`-nappia. Sijainteja taas pääsee muokkaamaan `List locations`-näkymässä `Edit location`-napista.

### Kaikkien kurssi-ilmoittautumisten tarkastelu

Kurssi-ilmoittautumisia pääsee tarkastelemaan painamalla yläpalkista `All registrations`.

### Ilmoittautumisten hakeminen

Ilmoittautumisia pääsee hakemaan asiakkaan nimen, sähköpostiosoitteen ja puhelinnumeron perusteella `All registrations`-näkymässä valitsemalla valikosta hakukriteerin, kirjoittamalla hakukenttään hakuehdon ja painamalla `Search`-nappia.
