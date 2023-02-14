-- This script lists all records with a name

SELECT score, name FROM second_table WHERE LENGTH(name) > 0 ORDER BY score DESC;
