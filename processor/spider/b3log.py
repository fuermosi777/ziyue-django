import basic

def crawl():
    return basic.std_rss_crawl('http://88250.b3log.org/blog-articles-rss.do')

if __name__ == "__main__":
    crawl()