import basic

def crawl():
    return basic.hard_crawl(url='http://www.cocoachina.com/ios/', list_select='.article-list ul li .newstitle a', title_select='.detail-main h2', body_select='.field_body', list_url_pre='http://www.cocoachina.com', remove_tags=[])

if __name__ == "__main__":
    crawl()