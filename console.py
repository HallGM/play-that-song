from models.request import Request
from models.song import Song
from models.artist import Artist
from models.user import User
from datetime import datetime
import repositories.artist_repository as artist_repository
import repositories.song_repository as song_repository
import repositories.user_repository as user_repository
import repositories.request_repository as request_repository

request_repository.delete_all()
user_repository.delete_all()
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

user1 = User("Garry", "my name is Garry")
user_repository.save(user1)

user2 = User("Bob", "I like music",)
user_repository.save(user2)

request1 = Request(song, user1, datetime.today())

request_repository.save(request1)

print(request1.display_time())

# print(artist_repository.select_all())
# print([vars(item) for item in song_repository.select_all()])
# print([vars(item) for item in user_repository.select_all()])
# print([vars(item) for item in request_repository.select_all()])