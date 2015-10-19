#!/usr/bin/env python
#urllib version
#import urllib

import sys
import codecs

#lxml version
import lxml
from lxml import html, etree
from lxml.html.clean import Cleaner

cleaner = Cleaner()
cleaner.javascript = True
cleaner.style = True

url = 'http://www.google.com'

#urllib version
#response = urllib.urlopen(url)
#webContent = response.read()

#lxml version
webContent = lxml.html.parse(url)
#cleaning page
cleanPage = cleaner.clean_html(webContent)
#result
Result = lxml.etree.tostring(cleanPage, pretty_print=True, method='html')

#urllib version
#f = open('index.html', 'w')
#f.write(webContent)

#lxml version
#f = open('index_lxml.html', 'w')
#f.write(Result)
sys.stdout.write(Result)
#f.close()

#urllib version
#print webContent

#lxml version
#print Result
