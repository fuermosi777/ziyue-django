import basic

def crawl():
    return basic.std_rss_crawl('http://app.ikanchai.com/?app=rss&controller=index&action=feed')

if __name__ == "__main__":
    crawl()