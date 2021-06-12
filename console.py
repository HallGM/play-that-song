from models.song import Song
from models.artist import Artist
from datetime import datetime
import repositories.artist_repository as artist_repository
import repositories.song_repository as song_repository

song_repository.delete_all()
artist_repository.delete_all()

bon_jovi = Artist("Bon Jovi")
artist_repository.save(bon_jovi)

lady_gaga = Artist("Lady Gaga")
artist_repository.save(lady_gaga)

the_beatles = Artist("The Beatles")
artist_repository.save(the_beatles)

song = Song("Livin' on  Prayer", bon_jovi, datetime(2020, 12, 25))
song_repository.save(song)

song2 = Song("Bad Romance", lady_gaga, datetime(2020, 12, 26))
song_repository.save(song2)

# print(artist_repository.select_all())
print([vars(item) for item in song_repository.select_all()])