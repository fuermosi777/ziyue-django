import basic

def crawl():
    return basic.std_rss_crawl('http://drops.wooyun.org/feed')

if __name__ == "__main__":
    crawl()