import basic

def crawl():
    return basic.std_rss_crawl('http://rss.aqee.net/')

if __name__ == "__main__":
    crawl()