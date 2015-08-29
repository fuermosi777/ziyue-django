import basic

def crawl():
    return basic.std_rss_crawl('http://13tech.com.cn/?feed=rss2')

if __name__ == "__main__":
    crawl()