import basic

def crawl():
    return basic.std_rss_crawl('http://coolshell.cn/feed')

if __name__ == "__main__":
    crawl()