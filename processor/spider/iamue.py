import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.iamue.com/feed', title_select='h1.post-title', body_select='section.article-content', remove_tags=['div'])

if __name__ == "__main__":
    crawl()