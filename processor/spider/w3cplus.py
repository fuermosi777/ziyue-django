import basic

def crawl():
    return basic.std_rss_crawl('http://www.w3cplus.com/rss.xml', should_unescape=True)

if __name__ == "__main__":
    crawl()