import basic

def crawl():
    return basic.hard_crawl(
        url='http://www.w3ctech.com/', 
        list_select='.topic_list_content h2.topic_title a', 
        list_url_pre='http://www.w3ctech.com', 
        title_select='.topic_info h1', 
        body_select='.topic_detail .callout'
    )

if __name__ == "__main__":
    crawl()