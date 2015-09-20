import basic

def crawl():
    return basic.std_rss_crawl('http://solidot.org.feedsportal.com/c/33236/f/556826/index.rss', should_unescape=True)

if __name__ == "__main__":
    crawl()