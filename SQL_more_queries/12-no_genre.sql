-- Enumerar todos los shows en la DB sin generosUSE hbtn_0d_tvshows;

SELECT tv_shows.title, NULL AS genre_id
FROM tv_shows
WHERE tv_shows.id NOT IN (SELECT show_id FROM tv_shows_genres)
ORDER BY tv_shows.title ASC, genre_id ASC;