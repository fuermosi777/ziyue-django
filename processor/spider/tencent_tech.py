import basic

def crawl():
    return basic.std_rss_crawl('http://n.rss.qq.com/rss/tech_rss.php')

if __name__ == "__main__":
    crawl()