import basic

def crawl():
    return basic.std_rss_crawl('http://app.iheima.com/?app=rss&controller=rssa&action=index')

if __name__ == "__main__":
    crawl()