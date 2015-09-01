import basic

def crawl():
    return basic.std_rss_crawl('http://www.igeek.com.cn/portal.php?mod=rss&catid=')

if __name__ == "__main__":
    crawl()