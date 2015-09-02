import basic

def crawl():
    return basic.list_rss_crawl('http://www.idcps.com/rss', '.main h1', '.main .content')

if __name__ == "__main__":
    crawl()