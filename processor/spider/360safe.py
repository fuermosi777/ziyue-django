import basic

def crawl():
    return basic.std_rss_crawl('http://blogs.360.cn/360safe/feed/', should_unescape=True)

if __name__ == "__main__":
    crawl()