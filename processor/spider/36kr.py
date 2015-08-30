import basic

def crawl():
    return basic.std_rss_crawl('http://36kr.com/feed', should_unescape=True)

if __name__ == "__main__":
    crawl()