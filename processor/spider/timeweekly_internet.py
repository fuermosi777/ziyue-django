import basic

def crawl():
    return basic.hard_crawl(url='http://www.time-weekly.com/html/newmedia/', list_select='ul.sumlist01 li a', title_select='.sumlist01 h1', body_select='.content', list_url_pre='', remove_tags=[])

if __name__ == "__main__":
    crawl()