import re





def mail(x):
    p = re.compile('[A-Za-z0-9#$%&*+-/=?^_{|}~]{1,100}\@[A-Za-z0-9]{1,100}\.[A-Za-z0-9]{1,10}')
    a=p.findall(x, re.MULTILINE)
    print(a)





def main(z):
    ##z = input()
    mail(z)


z =   \
    '''
i    .
    Kontakt adresa za pitanja o upisu na diplomske studije je      diplomski.upisi@fer.hr
    asdf.gmail@gmail.com apoikl@fer.hr.

     Kandidati koji su se prijavili na ljetnom upisnom roku za u    '''
print(z)
main(z)
