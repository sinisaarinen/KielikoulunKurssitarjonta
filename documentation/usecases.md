# Käyttötapaukset

## Käyttötapaukset rooleittain

### 1. Asiakas

1.1 Asiakas voi rekisteröityä järjestelmään

~~~~sql

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS
account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS
account_password, account.role AS account_role 
FROM account 
WHERE account.username = ?

INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, 
CURRENT_TIMESTAMP, ?, ?, ?, ?)

~~~~

1.2 Asiakas voi kirjautua järjestelmään

~~~~sql

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password, account.role AS account_role 
FROM account 
WHERE account.id = ?

~~~~

1.2 Asiakas voi tarkastella lisättyjä kursseja

~~~~sql

SELECT course.id AS course_id, course.date_created AS course_date_created, course.date_modified AS course_date_modified,
course.name AS course_name, course.coursecode AS course_coursecode, course.language AS course_language, course.level AS
course_level, course.spots AS course_spots, course.course_location AS course_course_location, course.description AS
course_description, course.registrationsopen AS course_registrationsopen FROM course

~~~~

- Asiakas voi hakea kursseja
  - kurssin nimen perusteella
  - kurssikoodin perusteella
  - opetuskielen perusteella
  - tason perusteella
  
1.3 Kursseille ilmoittautuminen

- Käyttäjä voi ilmoittautua kurssille, jos ilmoittautuminen on auki

1.4 Kurssi-ilmoittautumisten tarkastelu

- Käyttäjä voi tarkastella omia kurssi-ilmoittautumisiaan

1.5 Kurssi-ilmoittautumisten muokkaus (ei toimi vielä)

1.6 Kurssi-ilmoittautumisten poisto (ei toimi vielä)

### 2. Admin

2.1 Järjestelmään rekisteröityminen ja kirjautuminen

2.2 Kurssien ja sijaintien lisääminen

2.3 Kurssien ja sijaintien muokkaaminen

- Admin voi muokata kurssien ja sijaintien tietoja ja avata kurssille ilmoittautumisen

2.4 Kurssien ja sijaintien poistaminen

2.5 Kurssi-ilmoittautumisten tarkastelu

- Adminille on oma näkymä, jossa näkyvät kaikki kurssi-ilmoittautumiset

2.6 Kurssi-ilmoittautumisten hakeminen

- Admin voi hakea kurssi-ilmoittautumisia
  - Asiakkaan nimen perusteella
  - Asiakkaan puhelinnumeron perusteella
  - Asiakkaan sähköpostiosoitteen perusteella

2.7 Ilmoittautumisten yhteenvetojen tarkastelu

- Admin voi tarkastella etusivulla yhteenvetoja kurssi-ilmoittautumisista

~~~~sql

SELECT location.cityname, COUNT(Course.id) FROM Course LEFT JOIN location 
ON Course.course_location=location.id GROUP BY location.cityname

SELECT course.name, COUNT(Registration.id) FROM Registration LEFT JOIN course 
ON Registration.course_name=course.id GROUP BY course.name

SELECT course.name, COUNT(Registration.id) FROM Registration LEFT JOIN course 
ON Registration.course_name=course.id GROUP BY course.name ORDER BY Count(Registration.id) DESC LIMIT 3

~~~~
