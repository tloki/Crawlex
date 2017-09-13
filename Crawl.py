import Page

class Crawl:
    def __init__(url_arg, max_iter_arg, max_time_arg):
        self.max_iter = max_iter_arg
        self.max_time = max_time_arg
        self.start_url = url_arg
