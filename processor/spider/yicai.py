import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.yicai.com/rss/keji.xml', title_select='.news h1', body_select='.news .text', remove_tags=[])

if __name__ == "__main__":
    crawl()