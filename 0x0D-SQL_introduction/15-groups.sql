-- Counts the number of records with the same score in second_table and sorts by count (descending)
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
