import urllib, sys, chardet, argparse
from lxml.html import fromstring, tostring
from lxml.html.clean import Cleaner

def create_parser(): #Creating command line arguments parser
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?')

    return parser

def get_page(url): #Getting web-page with given url
    content = urllib.urlopen(url).read()
    Encoding = chardet.detect(content)['encoding']
    page = fromstring(content.decode(Encoding))
    page.make_links_absolute(url)

    return page

def create_cleaner(): #Creating html cleaner with noJavascript and noStyle option
    cleaner = Cleaner()
    cleaner.javascript = True
    cleaner.style = True

    return cleaner

def get_bare_page(page): #Cleaning web-page
    cleaner = create_cleaner()
    bare_page = cleaner.clean_html(page)

    return bare_page

def std_output(Result): #Printing clean page on standart output
    sys.stdout.write(Result)

def main():
    Result = '123'
    try:
        if __name__ == "barewebsite.core":
            parser = create_parser()
            arguments = parser.parse_args()
            if arguments.name:
                url = "{}".format (arguments.name)
                page = get_page(url)
                bare_page = get_bare_page(page)
                Result = tostring(bare_page, pretty_print=True, encoding='utf-8')
            else:
                Result = 'Web-page is not specified\n'
    except IOError:
        Result = 'Not a valid Web-page\n'
    except TypeError:
        Result = 'Check your network settings\n'
    #except:
    #    e = sys.exc_info()[0]
    #    Result = "Error: %s\n" % e
    std_output(Result)
    #f = open('result.html', 'w')
    #f.write(Result)
    #f.close()
