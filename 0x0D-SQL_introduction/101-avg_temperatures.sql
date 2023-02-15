-- This script displays average temps based on cities

USE hbtn_0c_0;
SOURCE temperatures.sql;
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
