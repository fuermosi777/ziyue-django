import basic

def crawl():
    return basic.std_rss_crawl('http://www.gao7.com/article/gkj/rss')

if __name__ == "__main__":
    crawl()