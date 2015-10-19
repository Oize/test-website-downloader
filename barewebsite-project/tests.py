from unittest import TestCase
from barewebsite.core import get_message

class BarewebsiteTestCase(TestCase):
    def test_barewebsite(self):
	self.assertEqual(get_message(), 'Hello World!')
