from re import compile, findall, MULTILINE, IGNORECASE
import urllib.request

class MailFinder:
    def __init__(self, source_arg):
        self.def_source = source_arg
        self.compile = compile(r'[A-Za-z0-9#$%&*+-=?^_{|}~]{1,100}\@[A-Za-z0-9]{1,100}\.[A-Za-z0-9]{1,10}', MULTILINE)

    def mail_finder(self):
        print(self.compile.findall(self.def_source))
        
if __name__ == '__main__':
    temp = MailFinder(urllib.request.urlopen(input()).read().decode('utf8'))
    temp.mail_finder()
