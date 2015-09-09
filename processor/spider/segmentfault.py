import basic

def crawl():
    return basic.std_rss_crawl('http://segmentfault.com/feeds/blogs', should_unescape=True)

if __name__ == "__main__":
    crawl()