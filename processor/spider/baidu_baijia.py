import basic

def crawl():
    url_list = get_list()
    res = []
    for u in url_list:
        res.append(basic.hard_scrape_post(url=u, title_select='h1', body_select='.article-detail', remove_tags='div'))
    return res

def get_list():
    data = basic.load_json('http://baijia.baidu.com/ajax/labellatestarticle?page=1&pagesize=20&prevarticalid=168862&flagtogether=1&labelid=3')
    res = []
    for d in data['data']['list']:
        res.append(d['m_display_url'])
    return res


if __name__ == "__main__":
    crawl()