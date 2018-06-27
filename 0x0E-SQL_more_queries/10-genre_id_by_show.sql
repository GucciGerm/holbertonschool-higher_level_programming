-- This script will list all shows contained in hbtn_0d_tvshows
-- Each record will display tv_shows.title - tv_show_genres.genre_id
-- Will be in ascending order from tv-shows title to tv-shows genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
