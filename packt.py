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
        for line in information.find_all("div"):
            if not line.find(class_='packt-js-countdown') and not line.find(class_='dots-main-book-price float-left'):
                print ("%s"% (line.text))


if __name__ == '__main__':
    book = Book()
    book.run()
