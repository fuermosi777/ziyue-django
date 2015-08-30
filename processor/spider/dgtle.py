import basic

def crawl():
    return basic.std_rss_crawl('http://www.dgtle.com/rss/dgtle.xml')

if __name__ == "__main__":
    crawl()