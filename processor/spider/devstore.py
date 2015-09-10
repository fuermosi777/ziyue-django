import basic

def crawl():
    return basic.hard_crawl(url='http://www.devstore.cn/essay/essayHome.html', list_select='dd.content h3 a', title_select='h1.title', body_select='.article_content', list_url_pre='http://www.devstore.cn', remove_tags=[])

if __name__ == "__main__":
    crawl()