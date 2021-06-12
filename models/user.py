class User:
    def __init__(self, username, bio, requests = None, id = None):
        self.username = username
        self.bio = bio
        if requests == None:
            self.requests = []
        else:
            self.requests = requests
        self.id = id
