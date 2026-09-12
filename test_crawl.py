import unittest
from crawl import normalize_url

class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_2(self):
        input_url = "http://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        self.assertEqual(actual, expected)

    def test_normalize_url_3(self):
        input_url = "duckduckgo.com"
        actual = normalize_url(input_url)
        expected = "www.duckduckgo.com"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()