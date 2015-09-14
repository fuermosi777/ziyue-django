from bs4 import BeautifulSoup as BS
import feedparser
import urllib2
import json
import HTMLParser
from processor import storer

# partial func

def load_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    }
    request = urllib2.Request(url, headers=headers)
    page = urllib2.urlopen(request)
    soup = BS(page.read())
    return soup

def load_feed(url):
    return feedparser.parse(url)

def load_json(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    }
    request = urllib2.Request(url, headers=headers)
    resp = urllib2.urlopen(request)
    data = json.loads(resp.read())
    return data

def unescape_body(body):
    '''
    change &lg; to < >...
    '''
    return HTMLParser.HTMLParser().unescape(body)

def rss_get_link_list(url):
    fd = load_feed(url)
    res = []
    for f in fd.entries:
        res.append(f.link)
    return res

def hard_scrape_list(url, list_select, list_url_pre):
    soup = load_soup(url)
    list = soup.select(list_select)
    res = []
    for l in list:
        res.append(list_url_pre + l.get('href'))
    return res

def hard_scrape_post(url, title_select, body_select, remove_tags):
    soup = load_soup(url)
    title = soup.select(title_select)[0].get_text()
    text_info = soup.select(body_select)[0]
    try:
        title = soup.select(title_select)[0].get_text()
        text_info = soup.select(body_select)[0]
    except:
        print 'Wrong hard scraping %s'%url
        return None
    # remove unwanted tags such as script, iframe... if needed
    try:
        for t in text_info:
            if t.name in remove_tags:
                t.extract()
    except:
        pass
    body = ''.join([unicode(x) for x in text_info.contents]) 
    return {
        'title': title,
        'body': body,
        'source': url,
    }

# complete crawler

# standard rss gives full content
# sometimes escaped HTML need to set 
# should_unescape = True
def std_rss_crawl(url, should_unescape=False):
    res = []
    fd = load_feed(url)
    for e in fd.entries[:30]:
        # sometimes all the content is in description
        # and there is no content at all
        if 'content' in e:
            content = e.content[0].value
        else:
            content = e.description

        # unescape
        if should_unescape:
            content = unescape_body(content)

        res.append({
            'title': e.title,
            'body': content,
            'source': e.link,
        })
    return res

# rss only gives link list
# not full content
def list_rss_crawl(url, title_select, body_select, remove_tags=[]):
    list = rss_get_link_list(url)
    res = []
    for l in storer.filter_list(list):
        post = hard_scrape_post(l, title_select=title_select, body_select=body_select, remove_tags=[])
        if post:
            res.append(post)
    return res

def hard_crawl(url, list_select, title_select, body_select, list_url_pre='', remove_tags=[]):
    list = hard_scrape_list(url, list_select, list_url_pre)
    res = []
    for l in storer.filter_list(list):
        post = hard_scrape_post(l, title_select=title_select, body_select=body_select, remove_tags=[])
        if post:
            res.append(post)
    return res