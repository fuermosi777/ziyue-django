import basic

def crawl():
    return basic.list_rss_crawl(url='http://www.jdon.com/rss', title_select='.post_warp .post_titlename h3 span', body_select='h1.tpc_content')

if __name__ == "__main__":
    crawl()