import basic

def crawl():
    return basic.hard_crawl(
        url='http://div.io/pro/index', 
        list_select='.hot-topics li span.topic-title a.title', 
        list_url_pre='', 
        title_select='.topic-main .topic-firstfloor-info h1', 
        body_select='.topic-firstfloor-detail'
    )

if __name__ == "__main__":
    crawl()