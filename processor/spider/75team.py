import basic

def crawl():
    return basic.std_rss_crawl('http://www.75team.com/weekly/rss.php')

if __name__ == "__main__":
    crawl()