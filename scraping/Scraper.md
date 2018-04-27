# Scraper PoC
This was just a fun little proof of concept to pull some data off a fishing website using my favorite Requests library plus BeautifulSoup4.  Also used the csv library to create a CSV of the output to consume later.

The data that I was looking for was on the Product Detail Pages, which don't appear in the sitemap.  So, I needed to get the Category Pages from the sitemap, then read those and parse for the PDP URL's.

It definitely helped that all of the data I was looking for was on the target site PDP HTML and I didn't need to deal with any JavaScript or get too crazy.

Here's how to do this scrape:
1. Run _get_urls_from_sitemap.py_ to get the pages of a certain type.
2. De-Dupe and Copy the specific ones into the urls array in the next step 
3. Run _get_descpages_from_catpages.py_ to get the specific URL's to scrape
4. De-Dupe and Copy the specific ones into the urls array in the next step
5. Run _scrape_test.py_ to pull out the data

### Upgrades:
* Roll all of this steps in this process together better
* Make the data transfer between steps automatic versus all of the manual cutting and pasting
* Probably add a time.sleep() in a few spots so if I was running a bigger scrape, I wouldn't clobber the site.
* Configure a user-agent like in this [link](https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python)
* Use a config file with the target info
* I'd probably store some of this stuff in a database, too


### Other Helpful Links:
* Web Scraping with Python by Ryan Mitchell (a reference book)
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* http://stackoverflow.com/questions/28875799/extract-title-tag-with-beautifulsoup
* http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html

