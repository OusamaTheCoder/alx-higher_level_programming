-- Lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT t.name
FROM tv_genres t
JOIN tv_show_genres g ON t.id = g.genre_id
JOIN tv_shows s ON g.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY t.name;
