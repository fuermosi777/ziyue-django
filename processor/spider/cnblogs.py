import basic

def crawl():
    return basic.std_rss_crawl('http://feed.cnblogs.com/blog/picked/rss')

if __name__ == "__main__":
    crawl()