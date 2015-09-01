import basic

def crawl():
    return basic.std_rss_crawl('http://techcrunch.cn/feed/')

if __name__ == "__main__":
    crawl()