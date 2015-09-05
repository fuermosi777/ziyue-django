import basic

def crawl():
    return basic.std_rss_crawl('http://blog.jobbole.com/feed/')

if __name__ == "__main__":
    crawl()