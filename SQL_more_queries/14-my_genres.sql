-- Enumerar todos los generos del show Dexter
USE hbtn_0d_tvshows;

SELECT tv_genres.name
FROM tv_genres
WHERE id IN (
    SELECT genere_id FROM tv_show_genres
    WHERE show_id = (SELECT id FROM tv_show WHERE title = 'Dexter' LIMIT 1)
)
ORDER BY tv_genres.name ASC;