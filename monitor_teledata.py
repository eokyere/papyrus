#!/usr/bin/env python

# download the page from http://192.168.10.1/ which redirects to main.cgi?mac_esn=0a003ed7cdf5
# parse the page
# update database. 
# if down make a note to send uptime info next time it is up
# if up, and there is a note to send a downtime email send


import re, urllib                      
from BeautifulSoup import BeautifulSoup as bs
from BeautifulSoup import NavigableString as ns

class Scraping(object):
    def parse(self, url, parser=None):
        if parser is None:
            parser = self.__get
        driver = self._a
        return driver(url, parser)

    def p(self, content, parser):
        soup = bs(self.__bs_preprocess(content))
        return parser(soup)
    
    def __parse(self, file, parser):
        f = open(file, 'r')
        content = f.read()
        f.close()
        return self.p(content, parser)
    
    def _a(self, url, parser):
        sock = urllib.urlopen(url)         
        content = sock.read()           
        sock.close()
        return self.p(content, parser)
    
    def __get(self, soup):
        return soup

    def __bs_preprocess(self, html):
        """remove distracting whitespaces and newline characters"""
        pat = re.compile('(^[\s]+)|([\s]+$)', re.MULTILINE)
        html = re.sub(pat, '', html)       # remove leading and trailing whitespaces
        html = re.sub('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">', '', html) # remove doctype pragma
        html = re.sub('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"', '', html) # remove doctype pragma
        html = re.sub('\n', ' ', html)     # convert newlines to spaces
                                           # this preserves newline delimiters
        html = re.sub('[\s]+<', '<', html) # remove whitespaces before opening tags
        html = re.sub('>[\s]+', '>', html) # remove whitespaces after closing tags
        return html 


def main():
    url = 'http://192.168.10.1/main.cgi?mac_esn=0a003ed7cdf5'
    sxp = Scraping()
    parser = None
    # //*[@id="RegisteredAP"]
    
    content = sxp.parse(url, parser)
    print content.find('span', id='RegisteredAP').string
        
if __name__ == "__main__":
    main()