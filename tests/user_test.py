import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("bob", "hello my name is bob", 5)

    def test_user_has_id(self):
        self.assertEqual(5, self.user.id)

    def test_user_has_name(self):
        self.assertEqual("bob", self.user.username)

    def test_user_has_bio(self):
        self.assertEqual("hello my name is bob", self.user.bio)