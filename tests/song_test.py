import unittest
from models.song import Song
from models.artist import Artist
from datetime import datetime


class TestSong(unittest.TestCase):
    def setUp(self):
        blur = Artist("Blur")
        self.song = Song("Song 2", blur, datetime(2020, 12, 25), 5)

    def test_song_has_id(self):
        self.assertEqual(5, self.song.id)

    def test_song_has_title(self):
        self.assertEqual("Song 2", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Blur", self.song.artist.name)
    
    def test_song_has_date(self):
        self.assertEqual(2020, self.song.last_played.year)
        self.assertEqual(12, self.song.last_played.month)
        self.assertEqual(25, self.song.last_played.day)
    
    def test_display_info(self):
        self.assertEqual(self.song.display_info(), "Song 2 by Blur")

