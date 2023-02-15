-- This script displays cities and the states they belong to

SELECT cities.id, cities.name, states.name
FROM cities LEFT JOIN states ON states.id = state_id
ORDER BY cities.id ASC;
