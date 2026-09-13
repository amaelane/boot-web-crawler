from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag
from typing import TypedDict

class PageData(TypedDict):
    url: str
    heading: str
    first_paragraph: str
    outgoing_links: list[str]
    image_urls: list[str]

def normalize_url(url):
    SplitResult = urlsplit(url)
    if "www" not in SplitResult.netloc:
        return "www." + SplitResult.netloc + SplitResult.path
    return SplitResult.netloc + SplitResult.path

def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    heading_tag = soup.find(["h1", "h2"])
    if heading_tag and isinstance(heading_tag, Tag):
        return heading_tag.get_text(strip=True)
    return ""

def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    if soup.main:
        paragraph_tag = soup.main.find("p")
    else:
        paragraph_tag = soup.find("p")
    if paragraph_tag and isinstance(paragraph_tag, Tag):
        return paragraph_tag.get_text(strip=True)
    return ""

def get_urls_from_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    urls = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            if href.startswith("http"):
                urls.append(href)
            else:
                urls.append(base_url + href)
    return urls

def get_images_from_html(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    images = []
    for img in soup.find_all("img"):
        src = img.get("src")
        if src:
            if src.startswith("http"):
                images.append(src)
            else:
                images.append(base_url + src)
    return images

def extract_page_data(html: str, page_url: str) -> PageData:
    heading = get_heading_from_html(html)
    first_paragraph = get_first_paragraph_from_html(html)
    urls = get_urls_from_html(html, page_url)
    images = get_images_from_html(html, page_url)
    return {
        "url": page_url,
        "heading": heading,
        "first_paragraph": first_paragraph,
        "outgoing_links": urls,
        "image_urls": images
    }