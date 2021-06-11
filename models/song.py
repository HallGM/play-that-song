class Song:
    def __init__(self, title, artist, last_played):
        self.title = title
        self.artist = artist
        self.last_played = last_played

    def display_info(self):
        return f"{self.title} by {self.artist.name}"