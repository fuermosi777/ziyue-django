import basic

def crawl():
    return basic.std_rss_crawl('http://iconmoon.com/blog2/feed.php')

if __name__ == "__main__":
    crawl()