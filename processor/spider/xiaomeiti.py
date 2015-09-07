import basic

def crawl():
    return basic.std_rss_crawl('http://www.xiaomeiti.com/rss/')

if __name__ == "__main__":
    crawl()