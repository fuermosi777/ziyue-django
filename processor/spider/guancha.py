import basic

def crawl():
    return basic.hard_crawl(url='http://www.guancha.cn/Science/list_1.shtml', list_select='.search_result_item a', title_select='h2.content-title1', body_select='.all-txt', list_url_pre='http://www.guancha.cn', remove_tags=[])

if __name__ == "__main__":
    crawl()