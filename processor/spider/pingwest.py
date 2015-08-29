import basic

def crawl():
    return basic.std_rss_crawl('http://www.pingwest.com/feed/')

if __name__ == "__main__":
    crawl()