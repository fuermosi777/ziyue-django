import basic

def crawl():
    return basic.hard_crawl(url='http://www.aliued.cn/', list_select='.latestpost > .post > .top > a.block', title_select='.blog-list-title h2', body_select='.entry', list_url_pre='', remove_tags=[])

if __name__ == "__main__":
    crawl()