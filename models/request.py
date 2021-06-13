class Request:
    def __init__(self, song, user, time, id = None):
        self.song = song
        self.user = user
        self.time = time
        self.played = False
        self.id = id

    def mark_as_played(self):
        self.played = True

    def display_time(self):
        return self.time.strftime("%I:%M %p %Zon %A, %d %B")