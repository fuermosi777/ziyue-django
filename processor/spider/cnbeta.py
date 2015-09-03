import basic

def crawl():
    return basic.list_rss_crawl(url='http://rss.cnbeta.com/rss', title_select='h2.news_title', body_select='section.article_content', remove_tags=[])

if __name__ == "__main__":
    crawl()