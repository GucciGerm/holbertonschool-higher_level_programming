-- This script will list all genres from hbtn_0d_tvshows and display the number
-- of shows linked to each
-- Results must be sorted in descending order
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name ORDER BY number_shows DESC;
