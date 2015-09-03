import basic

def crawl():
    return basic.std_rss_crawl('http://www.williamlong.info/rss.xml')

if __name__ == "__main__":
    crawl()