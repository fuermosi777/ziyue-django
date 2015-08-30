import basic

def crawl():
    return basic.std_rss_crawl('http://www.devtalking.com/feed.xml')

if __name__ == "__main__":
    crawl()