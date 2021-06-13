class Song:
    def __init__(self, title, artist, last_played = None, id = None):
        self.title = title
        self.artist = artist
        self.last_played = last_played
        self.id = id

    def display_info(self):
        return f"{self.title} by {self.artist.name}"

    def display_last_played(self):
        return self.last_played.strftime("%I:%M %p %Zon %A, %d %B")