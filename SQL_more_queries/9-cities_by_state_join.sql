-- Enumerar todas las ciudades que esten en la DB
USE hbtn_0d_usa;

SELECT cities.id, cities.name (
    SELECT name FROM states WHERE states.id = cities.state_id
) AS state_name
FROM cities
ORDER BY cities.id ASC;