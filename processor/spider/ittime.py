import basic

def crawl():
    return basic.hard_crawl(
        url='http://news.ittime.com.cn/', 
        list_select='.left-list a.img_212', 
        list_url_pre='http://news.ittime.com.cn', 
        title_select='.article h1', 
        body_select='.articlep'
    )

if __name__ == "__main__":
    crawl()