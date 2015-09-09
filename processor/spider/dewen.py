import basic

def crawl():
    return basic.std_rss_crawl('http://hp.dewen.io/?feed=rss2', should_unescape=True)

if __name__ == "__main__":
    crawl()