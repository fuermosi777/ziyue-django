import basic
from bs4 import BeautifulSoup as BS
from datetime import datetime

def crawl():
    list = basic.rss_get_link_list('http://www.infoq.com/cn/feed/articles')
    res = []
    for l in list:
        res.append(get_post(l))
    return res

def get_post(url):
    soup = basic.load_soup(url)
    title = soup.select('h1.general')[0].get_text()
    # delete div's div, iframe, script
    text_info = soup.find('div', {'class': 'text_info'})
    try:
        for t in text_info:
            if t.name in ['script', 'iframe', 'div']:
                t.extract()
    except:
        pass

    body = unicode(text_info)

    return {
        'title': title,
        'body': body,
        'source': url,
    }

if __name__ == "__main__":
    crawl()