import re


def mail(x):
    print(re.findall(r'\s[A-Za-z0-9]{1}[A-Za-z0-9.!#$%&+-/=?^_`{|}"~]{6,30}[A-Za-z0-9]{1}\@\w{3,40}\.\w{2,5}', x))


def main():
    z = input('tekst ')
    mail(z)

main()
