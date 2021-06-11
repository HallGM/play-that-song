class Request:
    def __init__(self, song, user, time):
        self.song = song
        self.user = user
        self.time = time
        self.played = False

    def mark_as_played(self):
        self.played = True