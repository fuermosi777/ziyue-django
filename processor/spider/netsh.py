import basic

def crawl():
    return basic.list_rss_crawl(url='http://blog.netsh.org/feed', title_select='a.titlelink', body_select='#post-text', remove_tags=['div']

if __name__ == "__main__":
    crawl()