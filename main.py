def main():
    print("Hello from boot-web-scraper!")

    import sys

    print("Script name:", sys.argv[0]) # example.py
    print("Arguments:", sys.argv[1:]) # -v

    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    if len(sys.argv) == 2:
        print(f"starting crawl of: {sys.argv[1]}")


if __name__ == "__main__":
    main()
