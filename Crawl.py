import Page
import networkx as nx

class Crawl:
    def __init__(self, url_arg, max_iter_arg, max_time_arg):
        self.max_iter = max_iter_arg
        self.max_time = max_time_arg
        self.start_url = url_arg
        self.graph = None
        self.page_array = []
        #self.home_page = Page.Page(0, url_arg)

    def crawl(self):
        page_queue = [self.start_url]
        visited_pages = set()
        found_pages = set()
        found_mails = set()

        while len(page_queue) > 0:
            print(len(page_queue))
            current_page = page_queue.pop(0)

            if current_page not in visited_pages:
                visited_pages |= {current_page}
                p = Page.Page(0, current_page)
                local_links = p.get_links()
                found_mails |= p.get_mails()

                for local_url in local_links:
                    if local_url not in visited_pages and local_url not in found_pages:
                        page_queue.append(local_url)
                        found_pages |= {local_url}
                        print(local_url)
                        print(found_mails)
                        
        print(visited_pages)
        return visited_pages

if __name__ == '__main__':
    c = Crawl('http://www.python.org', 10**6, 10**6)
    r = c.crawl()
    print(len(r))
