from urllib.parse import urlsplit

def normalize_url(url):
    SplitResult = urlsplit(url)
    if "www" not in SplitResult.netloc:
        return "www." + SplitResult.netloc + SplitResult.path
    return SplitResult.netloc + SplitResult.path