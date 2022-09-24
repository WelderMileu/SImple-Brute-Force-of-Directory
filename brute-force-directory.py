#!/usr/bin/python3
try:
    from time import process_time
    from sys import argv as param
    from progressbar import progressbar as pgr
    from termcolor import colored
    from requests import get

except Exception as err:
    print(err)

# python3 ./progress.py <url> <wordlist>

class Simple:
    def __init__(self, url, wordlist_file):
        try:
            self.wordlist = open(wordlist_file, 'r') 
            self.domain   = str(url)
            self.dic      = []
        
        except Exception as err:
            print(err)

    def main(self):
        try:
            for x in self.wordlist.readlines():
                self.dic.append(x)

            for i in pgr(self.dic):
                url  = '{}/{}'.format(self.domain, i.replace('\n', ''))
                r    = get(url)
                code = r.status_code

                if code == 200 or code == 301:
                    code_in_color = colored(code, 'cyan')
                    temp          = round(process_time(), 2)
                    result        = "\n [{}] {} | {}s".format(code_in_color, url, temp)

                    print(result)
    
        except Exception as err:
            print(err)

if __name__ == '__main__':
    url      = param[1]
    wordlist = param[2]

    Simple   = Simple(url, wordlist)
    Simple.main()
