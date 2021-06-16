class Request:
    def __init__(self, song, user, time, id=None, played=False):
        self.song = song
        self.user = user
        self.time = time
        self.played = played
        self.id = id

    def mark_as_played(self):
        self.played = True

    def display_time(self):
        return self.time.strftime("%I:%M %p %Zon %A, %d %B")

    def mark_as_unplayed(self):
        self.played = False
