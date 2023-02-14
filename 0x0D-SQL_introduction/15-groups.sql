-- This script lists the how many times a score appears

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
