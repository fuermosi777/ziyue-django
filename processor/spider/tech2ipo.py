import basic

def crawl():
    return basic.std_rss_crawl('http://tech2ipo.feedsportal.com/c/34822/f/641707/index.rss')

if __name__ == "__main__":
    crawl()