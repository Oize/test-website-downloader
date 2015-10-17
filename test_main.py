#!/usr/bin/env python
#urllib version
#import urllib

import sys
import codecs

#lxml version
import lxml.html
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
Result = lxml.html.tostring(cleanPage)

#urllib version
#f = open('index.html', 'w')
#f.write(webContent)

#lxml version
f = open('index_lxml.html', 'w')
#f.write(cleanPage)
print cleanPage
f.close()

#urllib version
#print webContent

#lxml version
#print Result
