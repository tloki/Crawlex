import Page
import networkx as nx
import matplotlib.pyplot as plt
from multiprocessing import Queue
import time
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
        self.links_iter =  []
        self.page_ranks =  []

        # self.home_page = Page.Page(0, url_arg)

    def print(self, item):
        print(item)
        self.q.put(item)

    def crawl(self):
        depth = 0
        page_queue = [(self.start_url, depth)]
        visited_pages = set()
        found_pages = set()
        found_mails = set()
        start = time()
        end = time()

        for i in range(20):
        #while page_queue>0 or self.max_depth >= depth or self.max_time >= end-start or self.max_iter >= local_iter
            self.print(len(page_queue))
            current_page, depth = page_queue.pop(0)
            self.graph.add_node(current_page)

            if current_page not in visited_pages:
                visited_pages |= {current_page}
                p = Page.Page(0, current_page)
                local_links = p.get_links()
                found_mails |= p.get_mails()

                for local_url in local_links:
                    self.graph.add_edge(current_page, local_url)
                    if local_url not in visited_pages and local_url not in found_pages:
                        self.links_iter.append(local_url)
                        self.page_ranks.append(1.0)
                        page_queue.append((local_url, depth+1))
                        found_pages |= {local_url}
                        self.print(local_url)
            end = time()

        self.print(visited_pages)

        self.pageRank(self.graph,self.links_iter)
        #prl = []
       # for i in range(len(self.links_iter)):
            #print(l[i].page_rank)
        #    prl.append(self.links_iter[i].page_rank * 300)
        for i in range(len(self.page_ranks)):
            self.page_ranks[i] *= 210
            #self.print(self.page_ranks[i])
        nx.draw_spring(self.graph, node_size=self.page_ranks, node_shape = 's')
        plt.savefig("graph.png", node_size=self.page_ranks)
        return visited_pages, found_mails

    def pageRank(self,graph_arg, list_arg):

        d = 0.77
        MAX_ITER = 15

        for k in range(MAX_ITER):
            for i in range(len(list_arg)):
                temp_pr = 0
                for j in range(len(list_arg)):
                    if j != i and graph_arg.has_edge(self.links_iter[j], self.links_iter[i]):
                        temp_pr += self.page_ranks[j] / graph_arg.out_degree(list_arg[j])
                temp_pr = (1 - d) + d * temp_pr

                self.page_ranks[i] = temp_pr

        return


if __name__ == '__main__':
    c = Crawl('icm.hr', 10**6, 10**6, 2000)
    r = c.crawl()
    # nx.draw_random(c.graph)
    plt.show()
