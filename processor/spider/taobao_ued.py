import basic

def crawl():
    return basic.std_rss_crawl('http://ued.taobao.org/blog/feed/')

if __name__ == "__main__":
    crawl()