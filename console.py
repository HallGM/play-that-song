from controllers.user_controller import users
from models.request import Request
from models.song import Song
from models.artist import Artist
from models.user import User
from datetime import date, datetime
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

beach_boys = Artist("Beach Boys")
artist_repository.save(beach_boys)

song1 = Song("Livin' on  Prayer", bon_jovi, datetime(2020, 12, 25))
song_repository.save(song1)

song2 = Song("You Give Love a Bad Name", bon_jovi, datetime(2021, 1, 8))
song_repository.save(song2)

song3 = Song("Bad Romance", lady_gaga, datetime(2020, 12, 26))
song_repository.save(song3)

song4 = Song("Poker Face", lady_gaga, None)
song_repository.save(song4)

song5 = Song("Hey Jude", the_beatles, datetime(2021, 2, 3))
song_repository.save(song5)

song6 = Song("Get Back", the_beatles, datetime(2021, 3, 1))
song_repository.save(song6)

song7 = Song("Strawberry Fields Forever", the_beatles, datetime(2021, 3, 6))
song_repository.save(song7)

song8 = Song("Let it Be", the_beatles, datetime(2020, 4, 2))
song_repository.save(song8)

song9 = Song("With a little help from my friends", the_beatles, datetime(2021, 4, 1))
song_repository.save(song9)

song10 = Song("Good Vibrations", beach_boys, datetime(2021, 3, 20))
song_repository.save(song10)

song11 = Song("Warmth of the Sun", beach_boys, datetime(2020, 10, 3))
song_repository.save(song11)

song12 = Song("I Get Around", beach_boys, datetime(2020, 11, 11))

user1 = User("Garry", "my name is Garry")
user_repository.save(user1)

user2 = User("Bob", "I like music")
user_repository.save(user2)

user3 = User("Pauline", "I am a robot")
user_repository.save(user3)

request1 = Request(song1, user1, datetime.today())
request2 = Request(song6, user2, datetime.today())

request_repository.save(request1)
request_repository.save(request2)

# print(request_repository.select_by_user(user1.id))

# print(request1.display_time())

# print(artist_repository.select_all())
# print([vars(item) for item in song_repository.select_all()])
# users = user_repository.select_all()
# print([vars(item) for item in users])
# print([vars(item) for item in request_repository.select_all()])

# song_repository.search("j")