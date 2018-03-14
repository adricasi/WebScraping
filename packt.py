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


    def run(self):
        # download the web page
        html = self.get_web("https://www.packtpub.com/packt/offers/free-learning")
        #parse it
        soup = bs4.BeautifulSoup(html, "lxml")
        information = soup.find("div","dotd-main-book-summary float-left")
        title_book = information.find("div","dotd-title")
        title = title_book.text
        print ("%s"% (title))

if __name__ == '__main__':
    book = Book()
    book.run()
