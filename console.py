from models.artist import Artist
import repositories.artist_repository as artist_repository

artist_repository.delete_all()

artist = Artist("Bon Jovi")
artist_repository.save(artist)

print(artist_repository.select_all())