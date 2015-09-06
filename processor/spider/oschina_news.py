import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.oschina.net/news/rss', title_select='.BlogTitle h1', body_select='.BlogContent', remove_tags=[])

if __name__ == "__main__":
    crawl()