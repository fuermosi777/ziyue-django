import xml.etree.ElementTree as ET
import basic

def crawl():
    return basic.std_rss_crawl('http://www.geekpark.net/rss')

if __name__ == "__main__":
    crawl()