# imported bs4 and BeautifulSoup as dependencies
# Helpful Links:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# http://stackoverflow.com/questions/28875799/extract-title-tag-with-beautifulsoup
# http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html


from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://www.tacklewarehouse.com/Keitech_Swing_Impact_FAT_Swimbait/descpage-KSIF.html').read()

soup = BeautifulSoup(r, 'html.parser')

#print soup.prettify()[0:1000]

print "Title: {}".format(
    soup.find("title")
)

print "Product Title: {}".format(
    soup.find("h1", attrs={"itemprop":"name"}).text
)


