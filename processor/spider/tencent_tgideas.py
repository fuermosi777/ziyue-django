import basic

def crawl():
    return basic.list_rss_crawl(url="http://tgideas.qq.com/rss.xml", title_select="header.hd h2.tit", body_select="section.bd", remove_tags=[])

if __name__ == "__main__":
    crawl()