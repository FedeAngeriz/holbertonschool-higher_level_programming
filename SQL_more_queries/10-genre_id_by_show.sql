-- Enumerar todos los shows que tengan al menos un genero vinculado
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;