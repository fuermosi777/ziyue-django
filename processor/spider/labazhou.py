import basic

def crawl():
    return basic.std_rss_crawl(url='http://www.labazhou.net/feed/')

if __name__ == "__main__":
    crawl()