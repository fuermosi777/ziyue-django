import basic

def crawl():
    return basic.list_rss_crawl(url='http://programmer.csdn.net/rss_programmer.html', title_select='.detail h1.title', body_select='.detail .news_content', remove_tags=[])

if __name__ == "__main__":
    crawl()