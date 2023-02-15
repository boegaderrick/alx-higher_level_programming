-- This script displays cities of california

SET @s = (SELECT id FROM states WHERE name = 'California');
SELECT id, name FROM cities WHERE state_id = @s ORDER BY id ASC;
