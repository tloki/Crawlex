# prvotna neka skica klase cvora grafa - odnosno same stranice
# sva objasnjenja su u komentarima


class Page:
    page_id = -1        # jedistven id. Dan pri inicijalizaciji.
    father_id = -1      # id čvora s kojeg je došao. Dan pri inicijalizaciji
    url = ""            # url same stranice... bilo bi dobro da bude u punom obliku pa se preko njega moze dalje kopati. Dan pri inicijalizaciji
    emails = []         # svi mailovi sa stranice
    links = []          # svi linkovi sa stranice
    page_rank = 1.0     # varijabla potrebna za pagerank algoritam (od stvari koje su jos potrebne, trebat ce nam i izlazni stupanj cvora
                        # za sto vec postoji naredba u networkxu (out_degree)  )

    # e sad ne znam kako tocno zelimo da bude koncipirano ovo sto sam napravio 2 liste za mailove i linkove i da se onda
    # preko njih kopa

    def __init__(self,id_arg,fid_arg,url_arg):
        self.page_id = id_arg
        self.father_id = fid_arg
        self.url = url_arg

    def get_mails(self):
        # funkcija za trazenje mailova... sve sto treba (url i lista koja pohranjuje mailove) vec je u klasi
        raise NotImplementedError

    def get_links(self):
        # funkcija za trazenje linkova, odnosno daljnje granjanje, crawlanje, iteriranje kako god
        # posprema u listu links
        # cim nadje novi link provjerava ima li vec takav cvor, ako ne on odmah radi i novi cvor (za father_id prosljeduje svoj id i tako se kod grana)
        raise NotImplementedError

# naravno sve ovo su neke idejice, pa ako nesto steka dogovorimo se jos
# nisam mogao raditi na funkciama get_mails i get_links jer za to trebamo parser i ono za tekst

# Abramovic

