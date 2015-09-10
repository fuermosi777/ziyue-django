import basic

def crawl():
    return basic.std_rss_crawl(url='http://www.oschina.net/news/rss?show=industry')

if __name__ == "__main__":
    crawl()