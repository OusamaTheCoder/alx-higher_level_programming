-- Lists all genres not linked to the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT t.name
FROM tv_genres t
WHERE t.id NOT IN (
    SELECT g.genre_id
    FROM tv_show_genres g
    JOIN tv_shows s ON g.show_id = s.id
    WHERE s.title = 'Dexter'
)
ORDER BY t.name;
