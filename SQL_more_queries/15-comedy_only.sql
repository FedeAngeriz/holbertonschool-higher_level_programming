-- Enumerar todos los shows de comedia
SELECT tv_shows.title
FROM tv_shows
WHERE id IN (
    SELECT show_id FROM tv_show_genres
    WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy' LIMIT 1)
)
ORDER BY tv_shows.title ASC;