    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
    # vim:set fileencoding=urf8 :
import urllib2
import bs4
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Book(object):
    """documentation TODO"""

    def get_web(self, url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html


    def run(self):
        #Download the web page
        html = self.get_web("https://www.packtpub.com/packt/offers/free-learning")
        #Parse it
        soup = bs4.BeautifulSoup(html, "lxml")
        information = soup.find("div","dotd-main-book-summary float-left")

        #Get the title and description of the book
        description = []
        for line in information.find_all("div"):
            if line.find("h2"):
                #Get title
                title = line.text
            elif not line.find(class_='packt-js-countdown'):
                #Get the information
                description.append(line.text)

        #Send Gmail message
        fromaddr = "provawebscraping@gmail.com"     #"YOUR EMAIL ADRESS"
        toaddr = "adriator6@gmail.com"              #"THE EMAIL ADDRESSS TO SEND TO"

        #Estructure of the message
        message = MIMEMultipart()
        message['From'] = fromaddr
        message['To'] = toaddr
        message ['Subject'] = title                         #The subject is the title of the book
        message.attach(MIMEText(description[0], 'plain'))   #The body of the message with the information below the title.
        #Login
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromaddr, "1234567qwertyu")  # server.login("YOUR EMAIL ADRESS", "YOUR PASSWORD")
        #Send the message
        text = message.as_string()
        server.sendmail(fromaddr, toaddr, text)  # server.sendmail("YOUR EMAIL ADRESS", "THE EMAIL ADDRESSS TO SEND TO", message to send)
        server.quit()



if __name__ == '__main__':
    book = Book()
    book.run()
