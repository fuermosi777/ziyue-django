import basic

def crawl():
    return basic.list_rss_crawl(url='http://88250.b3log.org/blog-articles-rss.do', title_select='title', body_select='section.article-body', remove_tags=[])

if __name__ == "__main__":
    crawl()