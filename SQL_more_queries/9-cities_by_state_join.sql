-- script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cties.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY id ASC;
