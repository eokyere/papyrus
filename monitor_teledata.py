#!/usr/bin/env python

import re, urllib                      
from BeautifulSoup import BeautifulSoup as bs
from BeautifulSoup import NavigableString as ns

class Scraping(object):
    def parse(self, url, parser=None):
        if parser is None:
            parser = self.__get
        reader = self._a
        return reader(url, parser)

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

# update database. 
# if down make a note to send uptime info next time it is up
# if up, and there is a note to send a downtime email send
def main():
    url = 'http://192.168.10.1/main.cgi?mac_esn=0a003ed7cdf5'
    sxp = Scraping()
    print sxp.parse(url, parser)
    
def parser(soup):
    status = soup.find('span', id='RegisteredAP').string
    return (status,
            parse_device_info(soup),
            parse_site_info(soup),
            parse_sm_stats(soup))

def parse_device_info(soup):
    return parse_section(soup, 'SectionDeviceInfo')

def parse_site_info(soup):
    return parse_section(soup, 'SectionSiteInfoStats')

def parse_sm_stats(soup):
    return parse_section(soup, 'SectionSubscriberModemStats')

def parse_section(soup, id):
    soup = soup.find('div', id=id).table.tbody.contents
    xs = [(x.contents[0].string, 
           x.contents[1].span.string) for x in soup]
    d = {}   
    for k, v in xs:
        d[k] = v
    return d  
    
if __name__ == "__main__":
    main()


    