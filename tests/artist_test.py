import unittest
from models.artist import Artist


class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Blur", 5)

    def test_artist_has_id(self):
        self.assertEqual(5, self.artist.id)

    def test_artist_has_name(self):
        self.assertEqual("Blur", self.artist.name)
