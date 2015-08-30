import basic

def crawl():
    return basic.std_rss_crawl('https://linux.cn/rss.xml')

if __name__ == "__main__":
    crawl()