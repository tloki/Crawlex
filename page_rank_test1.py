from class_test1 import Page
import networkx as nx
import matplotlib.pyplot as plt


MAX_ITER = 10  #broj iteracija page_rank algoritma

#zamisilio sam pageRank kao void funkciju koja nista ne vraca vec samo mijenja pagerank vrijednosti svakog cvora, elementa liste
#isto tako bilo bi dobro (mozda) da imamo posebno listu sa svim stranicama i posebno graf s tim elementima liste
# (uvjeren sam da je laksa iteracija i da je sve poslozenije i lakse je trazit stvari) -> tako sam i koncipirao sam pagerank
#i tako sam i igradio ovu sample listu

### kako pagerank funkcionira
# d - dampling factor
# (obično se stavlja 0.85)
#
# kod
# PR(A) = (1-d)+d(PR(T1)/C(T1)+...+PR(Tn)/C(Tn))
#
# PR(x) - page rank stranice x
# C(x) - broj linkova koji izlaze iz stranice x
# T1 ... Tn -> stranice koje pokazuju na stranicu A
#
#
# možemo početi s vrijednošču 1


#funkciji se prosljedjuje i lista i graf
def pageRank(graph_arg,list_arg):

    d = 0.85
    global MAX_ITER

    for k in range(MAX_ITER):

        for i in range(len(list_arg)):
            temp_pr = 0
            for j in range(len(list_arg)):
                if j != i and graph_arg.has_edge(l[j],l[i]):
                    temp_pr += list_arg[j].page_rank/graph_arg.out_degree(list_arg[j])
            temp_pr = (1-d) + d * temp_pr

            list_arg[i].page_rank=temp_pr

    return


#kreiranje sample liste iz koje se kreira i sam graf
l = []

l.append(Page(1, 0, "index"))
l.append(Page(2, 1, "biografija"))
l.append(Page(3, 1, "djela"))
l.append(Page(5, 3, "rana_djela"))
l.append(Page(6, 3, "kasna_djela"))
l.append(Page(4, 1, "kontakt"))
l.append(Page(7, 1, "slike"))

test_graf = nx.DiGraph()
test_graf.add_nodes_from(l)

test_graf.add_edge(l[0],l[1])
test_graf.add_edge(l[0],l[2])
test_graf.add_edge(l[0],l[5])
test_graf.add_edge(l[0],l[6])

test_graf.add_edge(l[1],l[0])
test_graf.add_edge(l[2],l[0])
test_graf.add_edge(l[5],l[0])
test_graf.add_edge(l[6],l[0])

test_graf.add_edge(l[2],l[3])
test_graf.add_edge(l[2],l[4])
#####

#poziv page_rank funkcije
pageRank(test_graf,l)

#prl lista je dosta sklepan nacin da matplotlib nacrta cvorove cija velicina prati page rank (jer treba proslijediti array)
#posto cemo u listu spremati kad i u graf nebi trebalo biti problema s indexima (da se pomijesaju recimo)
#na test primjeru radi i crta dobru sliku

prl = []
#ispisuje page_rank vrijednosti i radi prl listu
for i in range(len(l)):
    print(l[i].page_rank)
    prl.append(l[i].page_rank*300)

#printa info grafa -> broj cvorova edgova itd... za testiranje
print(nx.info(test_graf))

#crta graf
nx.draw(test_graf,node_size =prl)
plt.show()

#Abramovic