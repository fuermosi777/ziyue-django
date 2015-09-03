import basic
from processor import storer

def crawl():
    list = basic.hard_scrape_list(url='https://yowureport.com/category/public/', list_select='.archive-post > .thumbnail > a', list_url_pre='')
    res = []
    for l in storer.filter_list(list):
        soup = basic.load_soup(l)
        title = soup.select('h1.post-title')
        contents = soup.select('.article-content')
        body = ''
        for c in contents:
            body = body + unicode(c)
        res.append({
            'title': title,
            'body': body,
            'source': l
        })
    print res

if __name__ == "__main__":
    crawl()