from unittest import TestCase
from helloci import hello

class HelloTests(TestCase):
    def test_hello(self):
        name = hello.hello("gang")
        self.assertEquals("gang", name)

