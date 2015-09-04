import basic

def crawl():
    return basic.std_rss_crawl('http://sheilasun.me/rss/')

if __name__ == "__main__":
    crawl()