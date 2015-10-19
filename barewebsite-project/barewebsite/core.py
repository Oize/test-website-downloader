import urllib, sys, chardet
from lxml.html import fromstring, tostring
from lxml.html.clean import Cleaner

if __name__ == "__main__":
    if len (sys.argv) > 1:
        url = "{}".format (sys.argv[1])        

content = urllib.urlopen(url).read()
Encoding = chardet.detect(content)['encoding']
if Encoding != 'utf-8':
    content = content.decode(Encoding, 'replace').encode('utf-8')
page = fromstring(content)

cleaner = Cleaner()
cleaner.javascript = True
cleaner.style = True

barePage = cleaner.clean_html(page)
Result = tostring(barePage, pretty_print=True, encoding='utf-8')

sys.stdout.write(Result)
