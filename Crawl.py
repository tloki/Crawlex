import Page
import networkx as nx
import matplotlib.pyplot as plt
from multiprocessing import Queue

import warnings
warnings.filterwarnings("ignore")


class Crawl:
    def __init__(self, url_arg, max_iter_arg, max_time_arg, max_depth_arg, queue=Queue()):
        self.max_iter = max_iter_arg
        self.max_time = max_time_arg
        self.max_depth = max_depth_arg
        self.start_url = url_arg
        self.graph = None
        self.page_array = []
        self.q = queue
        self.graph = nx.DiGraph()

        # self.home_page = Page.Page(0, url_arg)

    def print(self, item):
        print(item)
        self.q.put(item)

    def crawl(self):
        page_queue = [self.start_url]
        visited_pages = set()
        found_pages = set()
        found_mails = set()
        links_iter = []

        for i in range(20):
            self.print(len(page_queue))
            current_page = page_queue.pop(0)
            self.graph.add_node(current_page)

            if current_page not in visited_pages:
                visited_pages |= {current_page}
                p = Page.Page(0, current_page)
                local_links = p.get_links()
                found_mails |= p.get_mails()

                for local_url in local_links:
                    self.graph.add_edge(current_page, local_url)
                    if local_url not in visited_pages and local_url not in found_pages:
                        links_iter.append(local_url)
                        page_queue.append(local_url)
                        found_pages |= {local_url}
                        self.print(local_url)

        self.print(visited_pages)
        return visited_pages, found_mails

if __name__ == '__main__':
    c = Crawl('icm.hr', 10**6, 10**6)
    r = c.crawl()
    nx.draw_random(c.graph)
    plt.show()
