-- This script will list all comedy shows in the hbtn_0d_tvshows database
-- Each record will display tv_shows.title
-- Results will be sorted in ascending order by show title
SELECT tv_shows.title
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
