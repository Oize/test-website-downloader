#Bare Website
##Description

Test website content downloader.
Functions:
 - get web-page url from command line;
 - download this web-page;
 - remove all styles and javascripts from the web-page;
 - print edited page to standart output.

##Installation

First install the XSLT library:

```
sudo apt-cache install libxslt1-dev
```

Unpack package archive with the following command:

```
tar xvzf barewebsite-1.0.tar.gz
```

Enter the resulting folder:

```
cd barewebsite-1.0/
```

Install package:

```
python setup.py install
```

##Usage

Terminal command example:

```
barewebsite http://your.web.page/
```
