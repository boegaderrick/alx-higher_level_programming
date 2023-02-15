-- This script shows the state/s with the hottest recorded temperature

SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
