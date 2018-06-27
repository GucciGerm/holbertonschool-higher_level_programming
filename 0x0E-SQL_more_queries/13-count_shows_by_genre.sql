-- This script will list all genres from hbtn_0d_tvshows and display the number
-- of shows linked to each
-- Results must be sorted in descending order
SELECT tv_genres.name as genre, COUNT(*) AS number_shows FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre ORDER BY number_shows DESC;
