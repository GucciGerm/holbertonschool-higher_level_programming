-- This script will list all shows, and all genres linked to that show
-- from our database hbtn_0d_tvshows
-- Each record should displau: tv_shows.title and tv_genres.name
-- Results will be sorted in ascending order by show title and the genre name
SELECT tv_shows.title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC;
