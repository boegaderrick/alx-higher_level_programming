-- This script converts a database to utf8

USE temp;
SELECT CONVERT(name USING utf8) FROM first_table;
