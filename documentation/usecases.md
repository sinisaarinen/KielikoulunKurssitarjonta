# Käyttötapaukset

## Käyttötapaukset rooleittain

### 1. Kaikki roolit

1.1 Käyttäjä voi rekisteröityä järjestelmään

~~~~sql

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS
account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS
account_password, account.role AS account_role 
FROM account 
WHERE account.username = ?

INSERT INTO account (date_created, date_modified, name, username, password, role) VALUES (CURRENT_TIMESTAMP, 
CURRENT_TIMESTAMP, ?, ?, ?, ?)

~~~~

1.2 Käyttäjä voi kirjautua järjestelmään

~~~~sql

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS 
account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS 
account_password, account.role AS account_role 
FROM account 
WHERE account.username = ? AND account.password = ?

~~~~

1.3 Käyttäjä voi tarkastella lisättyjä kursseja

~~~~sql

SELECT course.id AS course_id, course.date_created AS course_date_created, course.date_modified AS course_date_modified,
course.name AS course_name, course.coursecode AS course_coursecode, course.language AS course_language, course.level AS
course_level, course.spots AS course_spots, course.course_location AS course_course_location, course.description AS
course_description, course.registrationsopen AS course_registrationsopen FROM course

~~~~

1.4 Käyttäjä voi hakea kursseja
  - kurssin nimen perusteella
  - kurssikoodin perusteella
  - opetuskielen perusteella
  - tason perusteella
  
Esimerkki kyselystä, kun haetaan kurssin nimen perusteella:

~~~~sql

SELECT course.id AS course_id, course.date_created AS course_date_created, course.date_modified AS course_date_modified, 
course.name AS course_name, course.coursecode AS course_coursecode, course.language AS course_language, course.level AS 
course_level, course.spots AS course_spots, course.course_location AS course_course_location, course.description AS 
course_description, course.registrationsopen AS course_registrationsopen 
FROM course 
WHERE (course.name LIKE '%' || ? || '%')

~~~~

1.5 Käyttäjä voi tarkastella lisättyjä sijainteja

~~~~sql

SELECT location.id AS location_id, location.date_created AS location_date_created, location.date_modified AS 
location_date_modified, location.cityname AS location_cityname, location.location AS location_location 
FROM location

~~~~

### 2. Asiakas
  
2.1 Asiakas voi ilmoittautua kurssille, jos ilmoittautuminen on auki

~~~~sql

SELECT course.id AS course_id, course.date_created AS course_date_created, course.date_modified AS course_date_modified, 
course.name AS course_name, course.coursecode AS course_coursecode, course.language AS course_language, course.level AS 
course_level, course.spots AS course_spots, course.course_location AS course_course_location, course.description AS 
course_description, course.registrationsopen AS course_registrationsopen 
FROM course

INSERT INTO registration (date_created, date_modified, name, phonenumber, email, course_name, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)

~~~~

2.2 Asiakas voi tarkastella omia kurssi-ilmoittautumisiaan

~~~~sql

SELECT Course.name, Registration.name, Registration.phonenumber, Registration.email, Registration.id FROM Registration JOIN 
Course ON Registration.course_name=Course.id LEFT JOIN account ON account.id=Registration.account_id WHERE account.id = ? 
GROUP BY Course.name, Registration.name, Registration.phonenumber, Registration.email

~~~~

2.3 Asiakas voi muokata omia kurssi-ilmoittautumisiaan

~~~~sql

UPDATE registration SET date_modified=CURRENT_TIMESTAMP, name=?, email=? WHERE registration.id = ?

~~~~

2.4 Asiakas voi poistaa oman kurssi-ilmoittautumisensa

~~~~sql

DELETE FROM registration WHERE registration.id = ?

~~~~

### 3. Admin

3.1 Admin voi lisätä kursseja ja sijainteja

~~~~sql

INSERT INTO course (date_created, date_modified, name, coursecode, language, level, spots, course_location, description, 
registrationsopen) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?, ?, ?)

~~~~

~~~~sql

INSERT INTO location (date_created, date_modified, cityname, location) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)

~~~~

3.2 Admin voi avata kurssille ilmoittautumisen

~~~~sql

UPDATE course SET date_modified=CURRENT_TIMESTAMP, registrationsopen=? WHERE course.id = ?

~~~~

3.3 Admin voi muokata kursseja ja sijainteja

~~~~sql

UPDATE course SET date_modified=CURRENT_TIMESTAMP, name=?, coursecode=?, language=?, level=?, spots=?, registrationsopen=? WHERE course.id = ?

~~~~

~~~~sql

UPDATE location SET date_modified=CURRENT_TIMESTAMP, cityname=?, location=? WHERE location.id = ?

~~~~

3.4 Admin voi poistaa kursseja ja sijainteja

~~~~sql

DELETE FROM course WHERE course.id = ?

~~~~

~~~~sql

DELETE FROM location WHERE location.id = ?

~~~~

- Jos admin poistaa kurssin, poistuvat samalla myös kurssin mahdolliset ilmoittautumiset. Jos admin poistaa sijainnin, poistuvat samalla sijaintiin liittyvät kurssit ja ilmoittautumiset.

3.5 Admin voi tarkastella kaikkia kurssi-ilmoittautumisia

~~~~sql

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS 
account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS 
account_password, account.role AS account_role 
FROM account 
WHERE account.id = ?

SELECT registration.id AS registration_id, registration.date_created AS registration_date_created, registration.date_modified 
AS registration_date_modified, registration.name AS registration_name, registration.phonenumber AS registration_phonenumber, 
registration.email AS registration_email, registration.course_name AS registration_course_name, registration.account_id AS 
registration_account_id 
FROM registration

SELECT Course.name, Course.id FROM Registration JOIN Course ON Registration.course_name=Course.id GROUP BY Course.name

~~~~

3.6 Admin voi hakea kurssi-ilmoittautumisia
  - Asiakkaan nimen perusteella
  - Asiakkaan puhelinnumeron perusteella
  - Asiakkaan sähköpostiosoitteen perusteella
  
Esimerkki kyselystä, kun haetaan asiakkaan nimen perusteella:

~~~~sql

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS 
account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS 
account_password, account.role AS account_role 
FROM account 
WHERE account.id = ?

SELECT registration.id AS registration_id, registration.date_created AS registration_date_created, registration.date_modified 
AS registration_date_modified, registration.name AS registration_name, registration.phonenumber AS registration_phonenumber, 
registration.email AS registration_email, registration.course_name AS registration_course_name, registration.account_id AS 
registration_account_id 
FROM registration 
WHERE (registration.name LIKE '%' || ? || '%')

SELECT Course.name, Course.id FROM Registration JOIN Course ON Registration.course_name=Course.id GROUP BY Course.name

~~~~

3.7 Ilmoittautumisten yhteenvetojen tarkastelu

- Admin voi tarkastella etusivulla yhteenvetoja kurssi-ilmoittautumisista

~~~~sql

SELECT location.cityname, COUNT(Course.id) FROM Course LEFT JOIN location 
ON Course.course_location=location.id GROUP BY location.cityname

SELECT course.name, COUNT(Registration.id) FROM Registration LEFT JOIN course 
ON Registration.course_name=course.id GROUP BY course.name

SELECT course.name, COUNT(Registration.id) FROM Registration LEFT JOIN course 
ON Registration.course_name=course.id GROUP BY course.name ORDER BY Count(Registration.id) DESC LIMIT 3

~~~~

Ensimmäinen yllä olevista kyselyistä näkyy kaikille käyttäjille etusivulla roolista riippumatta.
