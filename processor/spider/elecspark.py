import basic

def crawl():
    return basic.std_rss_crawl('http://www.elecspark.com/feed/', should_unescape=True)

if __name__ == "__main__":
    crawl()