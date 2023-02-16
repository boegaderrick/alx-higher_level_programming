-- This script shows all genres associated with a show

-- SET @s = (SELECT id FROM tv_shows WHERE title = 'Dexter');
-- SELECT tv_genres.name FROM tv_genres JOIN tv_show_genres
-- ON tv_genres.id = tv_show_genres.genre_id WHERE tv_show_genres.show_id = 8
-- ORDER BY tv_genres.name ASC;

SELECT tv_genres.name FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;
