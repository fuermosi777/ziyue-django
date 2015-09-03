import basic

def crawl():
    return basic.std_rss_crawl('http://www.cyzone.cn/rss/?m=content&c=rss&a=init&rssid=1,2,3,4,5,6&moreinfo=1&pagesize=25')

if __name__ == "__main__":
    crawl()