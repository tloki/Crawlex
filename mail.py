import re


def url(x):
    if x[0]+x[1]+x[2]+x[3]+x[6]=='http/':
        print((re.split(r'(/*)', x))[0]+(re.split(r'(/*)', x))[1]+(re.split(r'(/*)', x))[2])
    else:
        print(re.split(r'(/*)',x)[0])

def mail(x):
    print(re.findall(r'[A-Za-z0-9.!#$%&+-/=?^_`{|}"~]{6,30}\@\w{3,40}\.\w{2,5}', x))

#def truefalse(x, y):
  #  if x[0]+x[1]+x[2]+x[3]+x[6]=='http/':
  #      for i in range(len(y.split())):
   #         return ((re.split(r'(/*)', i))[0]+(re.split(r'(/*)', i))[1]+(re.split(r'(/*)', i))[2])==x

    
        
        
def main():
    #h = input('upisite home url ')
   # u = input('parametar urlova ')
    #truefalse(h,u)
    #b = input('url ')
    #url(b)
    z = input('tekst ')
    mail(z)

main()
