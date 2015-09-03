import basic

def crawl():
    return basic.hard_crawl(url='http://www.keke289.com/info.html', list_select='article.article h2.article-title a', title_select='section.article-hd h2', body_select='section.article-bd', list_url_pre='http://www.keke289.com', remove_tags=['div'])

if __name__ == "__main__":
    crawl()