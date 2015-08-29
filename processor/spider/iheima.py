import basic

def crawl():
    return basic.std_rss_crawl('http://app.iheima.com/?app=rss&controller=rssa&action=index', should_unescape=True)

if __name__ == "__main__":
    crawl()