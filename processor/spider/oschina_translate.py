import basic

def crawl():
    return basic.std_rss_crawl(url='http://www.oschina.net/translate/rss?type=2')

if __name__ == "__main__":
    crawl()