#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB2
Created on 21/02/2017
@author: Aelxandru Martinas
'''

import urllib2
from bs4 import BeautifulSoup


class Client(object):

    """
    Downloads the page and prints the daily book name
    """

    def get_web(self, url):
        """
        Retrieves an HTML URL
        Returns HTML
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def search_parse(self, html):
        """
        Parses an html page
        """
        soup = BeautifulSoup(html,'html.parser')
        elements = soup.find_all("div","dotd-title")
        resultats = []

        for element in elements:
            title = str(element.find("h2"))
            newTitle = title.replace("\t","").replace("<h2>","") \
                        .replace("\n","").replace("</h2>","")
            resultats.append(newTitle)

        return resultats

    def run(self):
        """
        Prints the name of the daily book from
        www.packtpub.com/packt/offers/free-learning
        """
        html = self.get_web("http://www.packtpub.com/packt/offers/free-learning/")
        resultat = self.search_parse(html)
        print str(resultat[0])


if __name__ == "__main__":
    client = Client()
    client.run()
