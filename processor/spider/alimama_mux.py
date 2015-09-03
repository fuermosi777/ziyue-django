import basic

def crawl():
    return basic.std_rss_crawl('http://mux.alimama.com/feeds/posts.rss')

if __name__ == "__main__":
    crawl()