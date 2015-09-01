import basic

def crawl():
    return basic.std_rss_crawl('http://isux.tencent.com/feed/atom')

if __name__ == "__main__":
    crawl()