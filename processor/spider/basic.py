from bs4 import BeautifulSoup as BS
import feedparser
import urllib2
import json
from time import mktime
from datetime import datetime

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

# similar crawler

def std_rss_crawl(url):
    res = []
    fd = load_feed(url)
    for e in fd.entries:
        if 'content' in e:
            content = e.content[0].value
        else:
            content = e.description
        res.append({
            'title': e.title,
            'body': content,
            'source': e.link,
            'datetime': datetime.fromtimestamp(mktime(e.published_parsed)),
        })
    return res