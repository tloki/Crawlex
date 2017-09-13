import urllib.request
from html.parser import HTMLParser
from urllib.parse import urlparse
#prvotna neka skica klase cvora grafa - odnosno same stranice
#sva objasnjenja su u komentarima

#UPDATE

class Page(HTMLParser):
   # page_id = -1 #jedistven id. Dan pri inicijalizaciji.
   # father_id = -1  #id čvora s kojeg je došao. Dan pri inicijalizaciji
   # url = ""  #url same stranice... bilo bi dobro da bude u punom obliku pa se preko njega moze dalje kopati. Dan pri inicijalizaciji
   # emails = []  #svi mailovi sa stranice
   # links = [] #svi linkovi sa stranice
   # page_rank = 1.0 #varijabla potrebna za pagerank algoritam (od stvari koje su jos potrebne, trebat ce nam i izlazni stupanj cvora
                    #za sto vec postoji naredba u networkxu (out_degree)  )


    #e sad ne znam kako tocno zelimo da bude koncipirano ovo sto sam napravio 2 liste za mailove i linkove i da se onda
    #preko njih kopa


    def __init__(self,id_arg,url_arg):
        super().__init__()
        self.page_id = id_arg
        self.url = url_arg
        self.page_rank = 1.0
        self.emails = []
        self.links = []
        self.local_links = []
        self.all_links = []
        self.page_source = None

    def get_mails(self):
        #funkcija za trazenje mailova... sve sto treba (url i lista koja pohranjuje mailove) vec je u klasi
        return

    def get_links(self):
        self.url = self.network_location(self.url)
        self.feed(self.page_source.read().decode('utf8'))
        self.same_page_check(self.all_links)
        #funkcija za trazenje linkova, odnosno daljnje granjanje, crawlanje, iteriranje kako god
        #posprema u listu links
        #cim nadje novi link provjerava ima li vec takav cvor, ako ne on odmah radi i novi cvor (za father_id prosljeduje svoj id i tako se kod grana)
        return

    def __repr__(self):
        return self.url

    def check_url(self):

        url = self.url
        original_url = url

        if not url.startswith('http'):
            url = 'http://' + url
        self.page_source = urllib.request.urlopen(url)

        if self.page_source.getcode() == 301:
            url = url.replace('http://', 'https://')
            self.page_source = urllib.request.urlopen(url)

        self.url = url
        return self.page_source.getcode() == 200

    def network_location(self, url):
        o = urlparse(url, scheme='http')
        o = o.netloc
        return o

    def comparison(self, url):
        if self.network_location(self.url) == self.network_location(url):
            return True
        return False

    def same_page_check(self, all_links):
        for url in all_links:
            if self.comparison(url) == True:
                self.local_links.append(url)
        return self.local_links

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == 'href':
                self.all_links.append(value)
        return

#naravno sve ovo su neke idejice, pa ako nesto steka dogovorimo se jos
#nisam mogao raditi na funkciama get_mails i get_links jer za to trebamo parser i ono za tekst

#Abramovic

