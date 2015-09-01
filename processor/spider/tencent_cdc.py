import basic

def crawl():
    return basic.std_rss_crawl('http://cdc.tencent.com/?feed=rss2')

if __name__ == "__main__":
    crawl()