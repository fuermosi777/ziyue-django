import basic

def crawl():
    return basic.hard_crawl(url='https://www.oschina.net/news/list?show=industry', list_select='ul.List li h2 a', title_select='h1.OSCTitle', body_select='.NewsContent', list_url_pre='https://www.oschina.net', remove_tags=[])

if __name__ == "__main__":
    crawl()