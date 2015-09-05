import basic

def crawl():
    return basic.std_rss_crawl('http://beforweb.com/rss.xml')

if __name__ == "__main__":
    crawl()