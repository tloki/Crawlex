import urllib.request
from html.parser import HTMLParser
from urllib.parse import urlparse
from requests import Session, head
from urllib.error import URLError
from http.client import InvalidURL
from MailFinder import MailFinder
import time

# prvotna neka skica klase cvora grafa - odnosno same stranice
# sva objasnjenja su u komentarima


class Page(HTMLParser):
    # page_id = -1 #jedistven id. Dan pri inicijalizaciji.
    # father_id = -1  #id čvora s kojeg je došao. Dan pri inicijalizaciji
    # url = ""  #url same stranice... bilo bi dobro da bude u punom obliku pa se preko njega moze dalje kopati. Dan pri inicijalizaciji
    # emails = []  #svi mailovi sa stranice
    # links = [] #svi linkovi sa stranice
    # page_rank = 1.0 #varijabla potrebna za pagerank algoritam (od stvari koje su jos potrebne, trebat ce nam i izlazni stupanj cvora
    # za sto vec postoji naredba u networkxu (out_degree)  )

    # e sad ne znam kako tocno zelimo da bude koncipirano ovo sto sam napravio 2 liste za mailove i linkove i da se onda
    # preko njih kopa

    def __init__(self, id_arg, url_arg: str):
        super().__init__()
        self.page_id = id_arg
        self.this_page_url = url_arg
        self.url = url_arg
        self.page_rank = 1.0
        self.emails = []
        self.links = []
        self.local_links = []
        self.all_links = []
        self.page_source = None
        self.absolute_local_links = []
        self.absolute_all_links = []
        self.domain_url = self.network_location(self.url)
        self.skip_crawling = False
        self.skip_crawling = not self.check_url()
        if not self.skip_crawling:
            self.mail_prime = MailFinder(self.source_decoded)

    def check_links(self):
        if self.skip_crawling:
            return []
        # funkcija koja upotpunjava linkove
        # funkcija na pocetak lokalnih linkova koji nemaju scheme i netloc dodaje originalni url (tj. scheme i netlock)
        for nepotpuni_url in self.all_links:
            if '#' in nepotpuni_url:
                nepotpuni_url = nepotpuni_url[0:nepotpuni_url.index('#')]
            if nepotpuni_url.startswith('/') or nepotpuni_url.startswith('#'):
                self.absolute_all_links.append('http://' + self.domain_url + nepotpuni_url)
            elif nepotpuni_url.startswith('javascript'):
                self.absolute_all_links.append('http://' + self.domain_url + '/')
            else:
                self.absolute_all_links.append(nepotpuni_url)
        return self.absolute_all_links

    def get_mails(self):
        if  self.skip_crawling:
            return set()
        self.emails = self.mail_prime.mail_finder()

        return self.emails

    def get_links(self):
        #print('......', self.url, end=' ')
        if  self.skip_crawling:
            return []
        # self.url = self.network_location(self.url)
        if self.page_source is None:
            #TODO: should handle this...
            return []
        
        

        res = self.page_source
        http_message = res.info()

        #print('type="' + http_message.get_content_maintype() + '"')
        
        if not http_message.get_content_maintype() == 'text':
            self.skip_crawling = True
            return []

        # print(self.all_links)
        self.absolute_all_links = self.check_links()
        self.local_links = self.same_page_check(self.absolute_all_links)
        # TODO: add this to __init__?
        # funkcija za trazenje linkova, odnosno daljnje granjanje, crawlanje, iteriranje kako god
        # posprema u listu links
        # cim nadje novi link provjerava ima li vec takav cvor, ako ne on odmah radi i novi cvor (za father_id prosljeduje svoj id i tako se kod grana)
        return self.local_links

    def __repr__(self):
        return self.url

    def check_url(self):

        url = self.url
        
        if not url.startswith('http'):
            url = 'http://' + url

        response = head(url)
        
        if response.status_code == 301:
            url = url.replace('http://', 'https://')
            response = head(url)        

        if response.status_code == 200:
            contentType = response.headers['content-type']
            if not contentType.startswith('text'):
                self.skip_crawlng = True
                return False
            try:
                self.page_source = urllib.request.urlopen(url)

            except (URLError, InvalidURL) as e:
                return False

        else:
            return False
        try:
            self.source_decoded = self.page_source.read().decode('utf8')
            self.feed(self.source_decoded)
        except UnicodeDecodeError:
            pass

        self.url = url

        self.domain_url = self.network_location(self.url)

        return True

    def network_location(self, url):
        # print(url)
        o = urlparse(url)   # , scheme='http')
        o = o.netloc
        return o

    def comparison(self, url):
        if self.domain_url == self.network_location(url):
            return True
        return False

    def same_page_check(self, absolute_all_links):
        for url in absolute_all_links:
            if self.comparison(url):
                self.local_links.append(url)
        return self.local_links

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == 'href':
                self.all_links.append(value)
        return

# naravno sve ovo su neke idejice, pa ako nesto steka dogovorimo se jos
# nisam mogao raditi na funkciama get_mails i get_links jer za to trebamo parser i ono za tekst

# Abramovic

