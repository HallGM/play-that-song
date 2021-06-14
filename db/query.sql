SELECT songs.id as song_id, artists.id as artist_id, songs.title, artists.name 
FROM songs 
INNER JOIN artists 
ON songs.artist_id = artists.id
WHERE LOWER(artists.name) LIKE LOWER('%BON%')
OR LOWER(songs.title) LIKE LOWER('%BON%')