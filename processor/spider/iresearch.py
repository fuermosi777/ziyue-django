import basic

def crawl():
    return basic.std_rss_crawl('http://www.iresearch.cn/common/rss/column.xml')

if __name__ == "__main__":
    crawl()