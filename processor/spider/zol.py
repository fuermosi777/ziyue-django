import basic

def crawl():
    return basic.std_rss_crawl('http://rss.zol.com.cn/news.xml')

if __name__ == "__main__":
    crawl()