import requests
import urllib3
from bs4 import BeautifulSoup
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urls = [
'http://magento.packratbags.com/all-furniture/japanese-style-furniture/',
'http://magento.packratbags.com/the-raku-tatami-bed-in-japanese-style',
'http://magento.packratbags.com/the-raku-nightstand',

'https://magento.packratbags.com/all-furniture/japanese-style-furniture/',
'https://magento.packratbags.com/the-raku-tatami-bed-in-japanese-style',
'https://magento.packratbags.com/the-raku-nightstand',

'http://magento.packratbags.com/catalog/product/view/id/21/category/2',
'http://magento.packratbags.com/catalog/product/view/id/17',
'http://magento.packratbags.com/catalog/product/view/id/21',

'https://magento.packratbags.com/catalog/product/view/id/21/category/2',
'https://magento.packratbags.com/catalog/product/view/id/17',
'https://magento.packratbags.com/catalog/product/view/id/21',

'http://magento.packratbags.com/japanese-platform-beds.htm',
'http://magento.packratbags.com/total-sleep-systems.htm',
'https://magento.packratbags.com/japanese-platform-beds.htm',
'https://magento.packratbags.com/total-sleep-systems.htm',

'http://magento.packratbags.com/test-301-redirect.htm',
'http://magento.packratbags.com/test-302-redirect',
'https://magento.packratbags.com/test-301-redirect.htm',
'https://magento.packratbags.com/test-302-redirect',

]


# xmlDict = {}
urllist = []
r = requests.get("http://www.haikudesigns.com/sitemap.xml")
xml = r.text

soup = BeautifulSoup(xml, "html.parser")
loc_tags = soup.find_all("loc")
print("The number of sitemaps are {0}".format(len(loc_tags)))

for sitemap in loc_tags:
    print("Location: {}".format(sitemap.text))
    # print("Loc: {}".format(sitemap.findNext("loc").text))
    urllist.append(sitemap.text)

print(urllist)

urls = urllist

output_csv = open("Haiku-Crawl.csv", "w")
output_csv.write("URL, Code")

for url in urls:
    print("Url:  {}\n".format(url))

    response = requests.get(url, verify=False, allow_redirects=False)
    print("-Response: {}".format(response))
    output_csv.write("{}, {}\n".format(url, response.status_code))

    time.sleep(0.5)

output_csv.close()
