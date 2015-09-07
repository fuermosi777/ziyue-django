import basic

def crawl():
    return basic.std_rss_crawl('http://feeds.feedburner.com/techbang?fmt=xml')

if __name__ == "__main__":
    crawl()