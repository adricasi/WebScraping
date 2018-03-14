    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    # vim:set fileencoding=urf8 :
import urllib2
import bs4

class Book(object):
    """documentation TODO"""

    def get_web(self, url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html


    def almanac(self):
        # download the web page
        html = self.get_web("https://www.packtpub.com/packt/offers/free-learning")
        #parse it

if __name__ == '__main__':
    book = Book()
    book.run()
