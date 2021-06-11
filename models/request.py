class Request:
    def __init__(self, song, user, time, id = None):
        self.song = song
        self.user = user
        self.time = time
        self.played = False
        self.id = id

    def mark_as_played(self):
        self.played = True