import basic

def crawl():
    return basic.std_rss_crawl('http://www.oschina.net/blog/rss')

if __name__ == "__main__":
    crawl()