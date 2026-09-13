import unittest
from crawl import *

from bs4 import BeautifulSoup, Tag

class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        print(f"==================== \n test_normalize_url \n input_url: {input_url} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_normalize_url_2(self):
        input_url = "http://www.boot.dev/blog/path"
        actual = normalize_url(input_url)
        expected = "www.boot.dev/blog/path"
        print(f"==================== \n test_normalize_url_2 \n input_url: {input_url} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_normalize_url_3(self):
        input_url = "duckduckgo.com"
        actual = normalize_url(input_url)
        expected = "www.duckduckgo.com"
        print(f"==================== \n test_normalize_url_3 \n input_url: {input_url} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_heading_from_html(self):
        html = "<h1>This is a heading</h1>"
        actual = get_heading_from_html(html)
        expected = "This is a heading"
        print(f"==================== \n test_get_heading_from_html \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_2(self):
        html = "<h1>This is a heading</h1><p>This is a paragraph</p>"
        actual = get_heading_from_html(html)
        expected = "This is a heading"
        print(f"==================== \n test_get_heading_from_html_2 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_heading_from_html_3(self):
        html = "<h2>This is a subheading</h2>"
        actual = get_heading_from_html(html)
        expected = "This is a subheading"
        print(f"==================== \n test_get_heading_from_html_3 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html(self):
        html = "<p>This is a paragraph</p>"
        actual = get_first_paragraph_from_html(html)
        expected = "This is a paragraph"
        print(f"==================== \n test_get_first_paragraph_from_html \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_2(self):
        html = "<h1>This is a heading</h1><p>This is a paragraph</p>"
        actual = get_first_paragraph_from_html(html)
        expected = "This is a paragraph"
        print(f"==================== \n test_get_first_paragraph_from_html_2 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_3(self):
        html = "<h1>This is a heading</h1><p>This is a paragraph</p><p>This is another paragraph</p>"
        actual = get_first_paragraph_from_html(html)
        expected = "This is a paragraph"
        print(f"==================== \n test_get_first_paragraph_from_html_3 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_in_main_tag(self):
        html = """<html><body><h1>This is a heading</h1>
            <p>This is a paragraph</p>
            <main><p>This is a paragraph in the main tag</p></main>
            </body></html>"""
        actual = get_first_paragraph_from_html(html)
        expected = "This is a paragraph in the main tag"
        print(f"==================== \n test_get_first_paragraph_from_html_in_main_tag \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_urls_from_html(self):
        html = """<html><body>
            <a href="https://www.boot.dev/blog/path">Boot Dev Blog</a>
            <a href="/blog/path2">Boot Dev Blog 2</a>
            </body></html>"""
        base_url = "https://www.boot.dev"
        actual = get_urls_from_html(html, base_url)
        expected = ["https://www.boot.dev/blog/path", "https://www.boot.dev/blog/path2"]
        print(f"==================== \n test_get_urls_from_html \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_2(self):
        html = """<html><body>
            <a href="https://www.boot.dev/blog/path">Boot Dev Blog</a>
            <a href="/blog/path2">Boot Dev Blog 2</a>
            <a href="https://www.example.com">Example</a>
            </body></html>"""
        base_url = "https://www.boot.dev"
        actual = get_urls_from_html(html, base_url)
        expected = ["https://www.boot.dev/blog/path", "https://www.boot.dev/blog/path2", "https://www.example.com"]
        print(f"==================== \n test_get_urls_from_html_2 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_3(self):
        html = """<html><body>
            <a href="https://www.boot.dev/blog/path">Boot Dev Blog</a>
            <a href="/blog/path2">Boot Dev Blog 2</a>
            <a href="https://www.example.com">Example</a>
            <a href="/blog/path3">Boot Dev Blog 3</a>
            </body></html>"""
        base_url = "https://www.boot.dev"
        actual = get_urls_from_html(html, base_url)
        expected = ["https://www.boot.dev/blog/path", "https://www.boot.dev/blog/path2", "https://www.example.com", "https://www.boot.dev/blog/path3"]
        print(f"==================== \n test_get_urls_from_html_3 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_images_from_html(self):
        html = """<html><body>
            <img src="https://www.boot.dev/images/image1.jpg" />
            <img src="/images/image2.jpg" />
            </body></html>"""
        base_url = "https://www.boot.dev"
        actual = get_images_from_html(html, base_url)
        expected = ["https://www.boot.dev/images/image1.jpg", "https://www.boot.dev/images/image2.jpg"]
        print(f"==================== \n test_get_images_from_html \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_images_from_html_2(self):
        html = """<html><body>
            <img src="https://www.boot.dev/images/image1.jpg" />
            <img src="/images/image2.jpg" />
            <img src="https://www.example.com/images/image3.jpg" />
            </body></html>"""
        base_url = "https://www.boot.dev"
        actual = get_images_from_html(html, base_url)
        expected = ["https://www.boot.dev/images/image1.jpg", "https://www.boot.dev/images/image2.jpg", "https://www.example.com/images/image3.jpg"]
        print(f"==================== \n test_get_images_from_html_2 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_get_images_from_html_3(self):
        html = """<html><body>
            <img src="https://www.boot.dev/images/image1.jpg" />
            <img src="/images/image2.jpg" />
            <img src="https://www.example.com/images/image3.jpg" />
            <img src="/images/image4.jpg" />
            </body></html>"""
        base_url = "https://www.boot.dev"
        actual = get_images_from_html(html, base_url)
        expected = ["https://www.boot.dev/images/image1.jpg", "https://www.boot.dev/images/image2.jpg", "https://www.example.com/images/image3.jpg", "https://www.boot.dev/images/image4.jpg"]
        print(f"==================== \n test_get_images_from_html_3 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_extract_page_data(self):
        html = """<html><body>
            <h1>This is a heading</h1>
            <p>This is a paragraph</p>
            <a href="https://www.boot.dev/blog/path">Boot Dev Blog</a>
            <img src="https://www.boot.dev/images/image1.jpg" />
            </body></html>"""
        page_url = "https://www.boot.dev"
        actual = extract_page_data(html, page_url)
        expected = {
            "url": page_url,
            "heading": "This is a heading",
            "first_paragraph": "This is a paragraph",
            "outgoing_links": ["https://www.boot.dev/blog/path"],
            "image_urls": ["https://www.boot.dev/images/image1.jpg"]
        }
        print(f"==================== \n test_extract_page_data \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_extract_page_data_2(self):
        html = """<html><body>
            <h1>This is a heading</h1>
            <p>This is a paragraph</p>
            <a href="https://www.boot.dev/blog/path">Boot Dev Blog</a>
            <a href="/blog/path2">Boot Dev Blog 2</a>
            <img src="https://www.boot.dev/images/image1.jpg" />
            <img src="/images/image2.jpg" />
            </body></html>"""
        page_url = "https://www.boot.dev"
        actual = extract_page_data(html, page_url)
        expected = {
            "url": page_url,
            "heading": "This is a heading",
            "first_paragraph": "This is a paragraph",
            "outgoing_links": ["https://www.boot.dev/blog/path", "https://www.boot.dev/blog/path2"],
            "image_urls": ["https://www.boot.dev/images/image1.jpg", "https://www.boot.dev/images/image2.jpg"]
        }
        print(f"==================== \n test_extract_page_data_2 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_extract_page_data_3(self):
        html = """<html><body>
            <h1>This is a heading</h1>
            <p>This is a paragraph</p>
            <a href="https://www.boot.dev/blog/path">Boot Dev Blog</a>
            <a href="/blog/path2">Boot Dev Blog 2</a>
            <a href="https://www.example.com">Example</a>
            <img src="https://www.boot.dev/images/image1.jpg" />
            <img src="/images/image2.jpg" />
            </body></html>"""
        page_url = "https://www.boot.dev"
        actual = extract_page_data(html, page_url)
        expected = {
            "url": page_url,
            "heading": "This is a heading",
            "first_paragraph": "This is a paragraph",
            "outgoing_links": ["https://www.boot.dev/blog/path", "https://www.boot.dev/blog/path2", "https://www.example.com"],
            "image_urls": ["https://www.boot.dev/images/image1.jpg", "https://www.boot.dev/images/image2.jpg"]
        }
        print(f"==================== \n test_extract_page_data_3 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

    def test_extract_page_data_4(self):
        html = """<html><body>
            <h1>This is a heading</h1>
            <p>This is a paragraph</p>
            <a href="https://www.boot.dev/blog/path">Boot Dev Blog</a>
            <a href="/blog/path2">Boot Dev Blog 2</a>
            <a href="https://www.example.com">Example</a>
            <img src="https://www.boot.dev/images/image1.jpg" />
            <img src="/images/image2.jpg" />
            <img src="https://www.example.com/images/image3.jpg" />
            </body></html>"""
        page_url = "https://www.boot.dev"
        actual = extract_page_data(html, page_url)
        expected = {
            "url": page_url,
            "heading": "This is a heading",
            "first_paragraph": "This is a paragraph",
            "outgoing_links": ["https://www.boot.dev/blog/path", "https://www.boot.dev/blog/path2", "https://www.example.com"],
            "image_urls": ["https://www.boot.dev/images/image1.jpg", "https://www.boot.dev/images/image2.jpg", "https://www.example.com/images/image3.jpg"]
        }
        print(f"==================== \n test_extract_page_data_4 \n html: {html} \n Actual: {actual} \n Expected: {expected} \n ====================")
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()