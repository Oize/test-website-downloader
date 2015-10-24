from unittest import TestCase
from barewebsite import core

class BarewebsiteTestCase(TestCase):
    def test_create_parser(self):
        parser = core.create_parser()        
        self.assertEqual(str(type(parser)), "<class 'argparse.ArgumentParser'>")
    def test_create_cleaner(self):
        cleaner = core.create_cleaner()
        self.assertEqual(str(type(cleaner)), "<class 'lxml.html.clean.Cleaner'>")
    def test_get_page(self):
        url = 'http://www.google.com/'
        page = core.get_page(url)
        self.assertEqual(str(type(page)), "<class 'lxml.html.HtmlElement'>")
    def test_get_bare_page(self):
        url = 'http://www.google.com/'
        cleaner = core.create_cleaner()
        page = core.get_page(url)
        bare_page = cleaner.clean_html(page)
        self.assertEqual(str(type(page)), "<class 'lxml.html.HtmlElement'>")
