from datetime import datetime
import unittest
from models.request import Request
from models.artist import Artist
from models.song import Song
from models.user import User


class TestRequest(unittest.TestCase):
    def setUp(self):
        blur = Artist("Blur")
        song = Song("Song 2", blur, datetime(2020, 12, 25))
        user = User("bob", "hello my name is bob", [])
        self.time = datetime.today()
        self.request = Request(song, user, self.time, 5)

    def test_request_has_id(self):
        self.assertEqual(5, self.request.id)

    def test_request_has_song(self):
        self.assertEqual("Song 2", self.request.song.title)

    def test_request_has_user(self):
        self.assertEqual("bob", self.request.user.username)

    def test_request_has_time(self):
        self.assertEqual(self.time, self.request.time)

    def test_request_is_unplayed(self):
        self.assertEqual(False, self.request.played)
    
    def test_mark_as_played(self):
        self.request.mark_as_played()
        self.assertEqual(True, self.request.played)