import sys
import requests

headers = {"User-Agent": "BootCrawler/1.0"}

def main():
    print("Welcome to boot-web-scraper!")

    #print("Script name:", sys.argv[0]) # example.py
    #print("Arguments:", sys.argv[1:]) # -v

    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    if len(sys.argv) == 2:
        print(f"Starting crawl of: {sys.argv[1]}")

    get_html(sys.argv[1])


def get_html(url) -> str:
    response = requests.get(url, headers=headers)

    if response.status_code >= 400:
        raise Exception(f"Error fetching {url}: {response.status_code}")
    elif response.headers.get("Content-Type") != "text/html":
        raise Exception(f"Error fetching {url}: Content-Type is not text/html")
    return response.text

if __name__ == "__main__":
    main()
