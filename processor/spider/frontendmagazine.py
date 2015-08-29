import basic
from datetime import datetime

def crawl():
    url = 'http://zhuanlan.zhihu.com/api/columns/FrontendMagazine/posts'
    data = basic.load_json(url)
    res = []
    for d in data:
        res.append({
            'title': d['title'],
            'datetime': datetime.strptime(d['publishedTime'], '%Y-%m-%dT%H:%M:%S+08:00'),
            'body': d['content'],
            'source': 'http://zhuanlan.zhihu.com%s'%d['url'],
            'feature': d['titleImage'],
        })
    print res
    return res

if __name__ == "__main__":
    crawl()