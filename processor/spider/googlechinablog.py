import basic

def crawl():
    return basic.std_rss_crawl('http://googlechinablog.blogspot.com/feeds/posts/default?alt=rss', should_unescape=True)

if __name__ == "__main__":
    crawl()