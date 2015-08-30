from bs4 import BeautifulSoup as BS
import feedparser
import urllib2
import json
from time import mktime
from datetime import datetime
import HTMLParser

# partial func

def load_soup(url):
    print 'start loading soup %s'%url
    page = urllib2.urlopen(url)
    soup = BS(page.read())
    print 'finish loading soup %s'%url
    return soup

def load_feed(url):
    return feedparser.parse(url)

def load_json(url):
    resp = urllib2.urlopen(url)
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

def hard_scrape_post(url, title_select, body_select, datetime_select, date_format):
    pass

# complete crawler

def std_rss_crawl(url, should_unescape=False):
    res = []
    fd = load_feed(url)
    for e in fd.entries:
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
            'datetime': datetime.fromtimestamp(mktime(e.published_parsed)),
        })
    return res