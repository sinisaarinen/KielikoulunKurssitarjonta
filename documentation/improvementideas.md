# Rajoitukset ja jatkokehitysideat

Tämä dokumentti esittelee työn nykyisiä rajoituksia ja puutteita sekä jatkokehitysideoita niiden parantamiseksi. Jatkokehitysideat on kirjoitettu sovelluksen nykyisten rajoitusten ja puutteiden pohjalta.

## Roolit

Sovellukseksessa on tällä hetkellä roolit ainoastaan kahdenlaisille käyttäjille: admineille ja asiakkaille. Sovellukseen voisi lisätä admin- ja client-roolien lisäksi organizer-roolin, joka on räätälöity kielikursseja järjestäville tahoille.
Tällä roolilla olisi valtuudet lisätä kursseja ja sijainteja sekä muokata ja poistaa itse lisäämiään kursseja ja sijainteja sekä hallita omien kurssiensa ilmoittautumisia.
Vain admin-oikeudellisella käyttäjällä olisi siis valtuudet kaikkien kurssien, sijaintien ja ilmoittautumisten hallintaan.

## Rekisteröitymisen kehittäminen

Tällä hetkellä rekisteröitymään pääsee sekä admin- että client-rooleihin, joka ei tietenkään normaalisti saa olla mahdollista. Lisäksi rekisteröitymiseen vaaditaan ainoastaan käyttäjän nimi, käyttäjänimi ja salasana. Salasanalla ei ole myöskään mitään muita turvallisuusvaatimuksia kuin pituus. Rekisteröitymistä voisi kehittää siten, että rekisteröitymään pääsee ainoastaan client-rooliin ja rekisteröitymiseen vaaditaan enemmän tietoa, kuten käyttäjän sähköpostiosoite, koko nimi, syntymäaika ja osoite. Myös Facebookin tai muun sovelluksen kautta tunnistautuminen ja rekisteröityminen voitaisiin tehdä mahdolliseksi. Lisäksi rekisteröitymisestä voisi lähettää käyttäjälle vahvistusviestin sähköpostiin.

## Kurssien listauksen kehittäminen

Kurssien listaus on nykyisellään sellainen, että kaikki tiedot näkyvät käyttäjille samalla sivulla. Listausta voisi kehittää siten, että listaussivulla näkyy kursseista vaan tärkeimmät tiedot, ja kurssin nimeä klikkaamalla avautuu uusi näkymä, jossa on kattavammin tietoa kurssista.

Kurssien tiedoista puuttuu tällä hetkellä nykyinen paikkatilanne sekä kurssin päivämäärät. Listaukseen voisikin lisätä myös tiedon paikkatilanteesta (ilmoittautumisia tällä hetkellä/maksimimäärä) sekä kurssin tarkan ajankohdan.

## Kurssi-ilmoittautumisen kehittäminen

Asiakas näkee tällä hetkellä omat ilmoittautumisensa ainoastaan kirjautumalla sisään sovellukseen ja avaamalla My registrations -näkymän. Sovellukseen voisi lisätä toiminnon, joka lähettää automaattisen sähköpostiviestin asiakkaille vahvistuksena kurssi-ilmoittautumisesta. 

Kursseille voi myös tällä hetkellä ilmoittautua rajattomasti paikkamäärästä huolimatta. Ilmoittautumista voisi kehittää myös siten, että kurssille voi ilmoittautua vain, jos kurssilla on tilaa eli ilmoittautumismäärä ei ylitä kurssin paikkamäärää.

Tällä hetkellä sama käyttäjä pystyy rekisteröitymään samalle kurssille useaan kertaan. Tämän voisi korjata niin, että sama henkilö ei voi ilmoittautua samalle kurssille kuin kerran. Toisaalta jokaisen ilmoittautumisen yhteydessä käyttäjältä kysytään koko nimi, sähköpostiosoite ja puhelinnumero, joten tällä hetkellä yksi käyttäjä voi periaatteessa ilmoittaa esimerkiksi ystävänsä kurssille ilman, että tämän pitää itse rekisteröityä järjestelmään.

## Hakutoimintojen kehittäminen

Eri hakutoiminnot eivät ole nykyisellään täysin kattavia. Kurssien hakutoimintoa voisi kehittää lisäämällä hakukriteeriksi ajankohdan ja kurssipaikkakunnan. Ilmoittautumisten hakutoimintoa taas voisi kehittää siten, että kurssi-ilmoittautumisia voidaan hakea esimerkiksi kurssin nimen ja sijainnin perusteella. Adminin hakutoimintoa ilmoittautumisten osalta voisi kehittää siten, että admin voi hakea ilmoittautumisia myös kurssin nimen perusteella.
