import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.digitaling.com/rss', title_select='.article_title h2', body_select='.article_con', remove_tags=[])
    return basic.std_rss_crawl()

if __name__ == "__main__":
    crawl()