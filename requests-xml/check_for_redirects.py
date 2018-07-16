import requests

import urllib3
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

for url in urls:
    print("Url:  {}".format(url))

    response = requests.get(url, verify=False, allow_redirects=False)
    print("-Response: {}".format(response))