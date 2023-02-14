-- This script converts a database to utf8

USE hbtn_0c_0;
SELECT CONVERT(name USING utf8) FROM first_table;
