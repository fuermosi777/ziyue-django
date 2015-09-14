import basic

def crawl():
    return basic.hard_crawl(url='http://www.cnetnews.com.cn/', list_select='#tab1 li > .qu_jx > a', title_select='h1.qu_ti', body_select='.qu_content_div', list_url_pre='http://www.cnetnews.com.cn', remove_tags=['div'])

if __name__ == "__main__":
    crawl()