import basic

def crawl():
    return basic.hard_crawl(url='http://www.oschina.net/blog/more?p=1', list_select='.BlogList li h3 a', title_select='title', body_select='.BlogContent', list_url_pre='', remove_tags=[])

if __name__ == "__main__":
    crawl()