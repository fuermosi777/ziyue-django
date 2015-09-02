import basic

def crawl():
    return basic.std_rss_crawl('http://feeds.appinn.com/appinns/?fmt=xml')

if __name__ == "__main__":
    crawl()