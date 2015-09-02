import basic
from datetime import datetime

def crawl():
    url = 'http://zhuanlan.zhihu.com/api/columns/FrontendMagazine/posts'
    data = basic.load_json(url)
    res = []
    for d in data:
        res.append({
            'title': d['title'],
            'body': d['content'],
            'source': 'http://zhuanlan.zhihu.com%s'%d['url'],
        })
    return res

if __name__ == "__main__":
    crawl()