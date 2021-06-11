import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("bob", "hello my name is bob", [])

    def test_user_has_name(self):
        self.assertEqual("bob", self.user.name)

    def test_user_has_bio(self):
        self.assertEqual("hello my name is bob", self.user.bio)
    
    def test_user_has_requests(self):
        self.assertEqual([], self.user.requests)