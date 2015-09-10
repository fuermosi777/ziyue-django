import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.oschina.net/news/rss?show=industry', title_select='h1.OSCTitle', body_select='.NewsContent', remove_tags=[])

if __name__ == "__main__":
    crawl()