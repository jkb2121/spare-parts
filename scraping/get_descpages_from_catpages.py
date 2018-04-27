from bs4 import BeautifulSoup
import requests

#
# Run this Second!
#
# From the get_urls_from_sitemap.py, we get a list of all of the Category Pages.  Now we're going to scrape those
# pages to get the URL's for any Product Detail Pages.#
#

# The target's name has been redacted
domain = 'http://www.redacted.com'

#
# More laziness.  Deduped and narrowed down.
#
urls = [
'/River2Sea/catpage-RIVERSEA.html',
'/River2Sea_Crankbaits/catpage-CRNKR2S.html',
'/River2Sea_Top_Water/catpage-TOPR2S.html',
'/River2Sea_Swimbaits/catpage-SWIMRIVER.html',
'/River2Sea_Spinner_Baits/catpage-SPINR2S.html',
'/River2Sea_Buzz_Baits/catpage-BZZR2S.html',
'/River2Sea_Hollow_Body_Frogs/catpage-HBFR2S.html',
'/River2Sea_Jigs/catpage-JIGR2S.html',
'/River2Sea_Terminal_Tackle/catpage-RIVERSTERM.html',
'/River2Sea_Soft_Baits/catpage-RIVERSOFT.html',
'/River2Sea_Apparel/catpage-R2SEAAPPARE.html',
'/Roboworm/catpage-ROBO.html',
'/Roboworm_Worms/catpage-SFWROBO.html',
'/Roboworm_Swimbaits/catpage-RSWIM.html',
'/Roboworm_Terminal_Tackle/catpage-TERMROBO.html'
]

#
# For each of these URL's, look for the product image link (I'm grabbing the link associated with the item image) and
# then picking out the target url from the href.
#

for xurl in urls:

    url = "{}{}".format(domain, xurl)
    r = requests.get(url).text

    soup = BeautifulSoup(r, 'html.parser')

    links = soup.findAll("a", {"class": "image_wrap"})
    for link in links:
        if link is None:
            continue

        # print("Link: {}".format(link))
        # print("---------------------------------------")
        urlpath = link["href"]
        # print("Urlpath: {}".format(urlpath))

        if not 'descpage' in urlpath:
            continue

        print("{}".format(urlpath))

        #
        # The output list of URL's from this get provided to the scrape_test.py program
        #


