from bs4 import BeautifulSoup
import requests

#
# Run this one First!
#
# Quick and easy, read the sitemap file and pull out the Category Page URL's that we are looking to target
# If the page path doesn't contain the right keyword, we skip it because it is not a Category Page.
#
domain = "http://www.redacted.com"

url = '{}/sitemap.xml'.format(domain)
r = requests.get(url).text

soup = BeautifulSoup(r, 'html.parser')

urls = soup.findAll("url")
for url in urls:

    # print("---------------------------------------")
    urlpath = url.loc.text

    if not 'catpage' in urlpath:
        continue

    print("URL: {}".format(urlpath))

    #
    # The resulting list of Category page URL's get provided to the get_descpages_from_catpages.py program
    #
