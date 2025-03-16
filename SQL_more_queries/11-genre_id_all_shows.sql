-- Enumerar todos los shows contenidos en la DB
SELECT tv_shows.title, (
    SELECT genre_id FROM tv_show_genres WHERE tv_show_genres.show_id = tv_shows.id LIMIT 1
) AS genre_id
FROM tv_shows
ORDER BY tv_shows.title ASC, genre_id ASC;