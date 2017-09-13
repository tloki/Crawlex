import Page
import networkx as nx

class Crawl:
    def __init__(self, url_arg, max_iter_arg, max_time_arg):
        self.max_iter = max_iter_arg
        self.max_time = max_time_arg
        self.start_url = url_arg
        self.graph = None
        self.page_array = []
        self.home_page = Page.Page(0, url_arg)
        
    def crawl(self):
        page_queue = [self.home_page]
        visited_pages = set()
        
        while len(page_queue) > 0:
            current_page = page_queue.pop(0)

            if current_page not in visited_pages:
                visited_pages |= {current_page}
                p = Page.Page(0, current_page)

                for i in p.get_links():
                    if i not in visited_pages:
                        page_queue.append(i)
