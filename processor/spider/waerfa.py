import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.waerfa.com/feed', title_select='h1.article-title a', body_select='article.article-content', remove_tags=['div'])

if __name__ == "__main__":
    crawl()