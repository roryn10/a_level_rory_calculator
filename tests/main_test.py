import unittest
from project import greeting


class TestGreeting(unittest.TestCase):
    def test_output(self):
        # Test for correct greeting
        self.assertEqual(greeting('sir'), "Hello sir!")
