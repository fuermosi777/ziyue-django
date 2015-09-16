import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.huxiu.com/rss/0.xml', title_select='h1.t-h1', body_select='.article_content', remove_tags=[])

if __name__ == "__main__":
    crawl()