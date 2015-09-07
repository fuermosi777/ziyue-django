import basic

def crawl():
    return basic.std_rss_crawl('http://www.yihaomen.com/feed.asp')

if __name__ == "__main__":
    crawl()