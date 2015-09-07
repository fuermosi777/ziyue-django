import basic

def crawl():
    return basic.std_rss_crawl('http://cn.engadget.com/rss.xml')

if __name__ == "__main__":
    crawl()