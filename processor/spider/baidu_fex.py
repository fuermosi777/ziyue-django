import basic

def crawl():
    return basic.std_rss_crawl('http://fex.baidu.com/feed.xml')

if __name__ == "__main__":
    crawl()