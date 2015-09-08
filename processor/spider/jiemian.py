import basic

def crawl():
    return basic.hard_crawl(url='http://www.jiemian.com/lists/65.html', list_select='.news-list .news-view.card .news-img a', title_select='.article-header h1', body_select='.article-content', list_url_pre='', remove_tags=[])

if __name__ == "__main__":
    crawl()