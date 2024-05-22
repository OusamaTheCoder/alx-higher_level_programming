-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT t.name, SUM(r.rate) AS rating
FROM tv_genres t
JOIN tv_show_genres sg ON t.id = sg.genre_id
JOIN tv_show_ratings r ON sg.show_id = r.show_id
GROUP BY t.name
ORDER BY rating DESC;
