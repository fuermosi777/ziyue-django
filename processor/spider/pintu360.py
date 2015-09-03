import basic

def crawl():
    return basic.std_rss_crawl('http://www.pintu360.com/rss/news')

if __name__ == "__main__":
    crawl()