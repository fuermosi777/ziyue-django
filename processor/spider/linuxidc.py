import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.linuxidc.com/rssFeed.aspx', title_select='h1.aTitle', body_select='#content', remove_tags=[])

if __name__ == "__main__":
    crawl()