-- Lists all records of second_table with a name value, ordered by score (descending)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;