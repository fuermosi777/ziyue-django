import basic

def crawl():
    return basic.std_rss_crawl('http://itindex.net/feed.jsp')

if __name__ == "__main__":
    crawl()