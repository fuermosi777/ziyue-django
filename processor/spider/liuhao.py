import basic

def crawl():
    return basic.std_rss_crawl(url='http://liuhao.im/feed/?cat=3')

if __name__ == "__main__":
    crawl()