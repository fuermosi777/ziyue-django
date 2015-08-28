from bs4 import BeautifulSoup as BS
import feedparser
import urllib2
import json

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
        res.append({
            'title': e.title,
            'body': e.content[0].value,
            'source': e.link
        })
    return res