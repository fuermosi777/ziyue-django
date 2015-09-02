import basic
from processor import storer

def crawl():
    return basic.hard_crawl('http://www.cnetnews.com.cn/', '#tab1 li .qu_jx a', '.qu_mid h1.qu_ti', body_select='.qu_content_div', list_url_pre='http://www.cnetnews.com.cn', remove_tags=['div'])

if __name__ == "__main__":
    crawl()