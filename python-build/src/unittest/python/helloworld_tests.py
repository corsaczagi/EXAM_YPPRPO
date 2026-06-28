from unittest import TestCase
from helloworld import say_hello

class TestHelloWorld(TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello World")