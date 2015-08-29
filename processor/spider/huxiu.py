import basic
from datetime import datetime

def crawl():
    res = []
    list = get_list()
    for l in list:
        res.append(get_post(l))
    return res

def get_list():
    res = []
    list = basic.load_json('http://m.api.huxiu.com/portal/1/1?client_ver=6&push_type=iOSRel')
    for l in list['content']:
        res.append('http://m.api.huxiu.com/article/%s?client_ver=6&push_type=iOSRel'%l['aid'])
    return res

def get_post(url):
    post = basic.load_json(url)['content']
    return {
        'title': post['title'],
        'body': post['content'],
        'source': post['url'],
        'feature': post['pic'],
        'datetime': datetime.fromtimestamp(int(post['dateline'])).strftime('%Y-%m-%d %H:%M:%S'),
    }

if __name__ == "__main__":
    crawl()