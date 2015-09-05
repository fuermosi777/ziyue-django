import basic

def crawl():
    return basic.hard_crawl(url='http://www.aliued.com/', list_select='.listbox ul li .listbox_img a', title_select='.title_top', body_select='.post_content', list_url_pre='', remove_tags=[])

if __name__ == "__main__":
    crawl()