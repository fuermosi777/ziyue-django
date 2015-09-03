import basic

def crawl():
    return basic.hard_crawl(url='http://www.ciweek.com/v7/list.jsp', list_select='dl h2 a', title_select='p.title', body_select='.text', list_url_pre='http://www.ciweek.com', remove_tags=[])

if __name__ == "__main__":
    crawl()