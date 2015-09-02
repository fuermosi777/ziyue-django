import basic

def crawl():
    return basic.std_rss_crawl('http://www.techweb.com.cn/rss/focus.xml')

if __name__ == "__main__":
    crawl()