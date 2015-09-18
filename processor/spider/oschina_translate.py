import basic

def crawl():
    list = rss_get_link_list(url='http://www.oschina.net/translate/rss?type=2')
    res = []
    for l in storer.filter_list(list):
        post = basic.hard_scrape_post('%s?print'%l, title_select='h1', body_select='TextContent', remove_tags=[])
        if post:
            res.append(post)
    return res

if __name__ == "__main__":
    crawl()