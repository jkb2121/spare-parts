import re
import requests

# Regexr:  https://regexr.com/
# (cool site I use to real-time hack with regular expressions)

# List of URL's that I want to Regular Expression test:

urls = [
    "https://cdn.shopify.com/s/files/1/0021/6504/7351/products/trick-worm-cherry-seed_608x544.jpg?v=1531854672",
    "https://cdn.shopify.com/s/files/1/0021/6504/7351/products/trick-worm-cotton-candy_576x544.jpg?v=1531854672",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/s-l1600_072c97c9-5dc0-4f44-bd32-779f61ebb566.jpg",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/s-l1600_528d332c-50bf-42cb-8095-0ae8c632587d.jpg",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/sunfish_1e583ab5-7011-4a85-9894-2d061337ba20.jpg",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/yellow_perch_1a63bf6e-1b22-4f7e-9610-4ee6903be355.jpg",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/Green_Pumpkin_d024ccf3-349e-4b75-b8b5-97f7cf18156d.jpg",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/mo_obsession.png",
    "https://cdn.shopify.com/s/files/1/0021/6504/7351/products/12476921905207_448x448.jpg?v=1535733596",
    "https://cdn.shopify.com/s/files/1/0021/6504/7351/products/12476921970743_448x448.jpg?v=1535733596",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/KGrHqN_p8FC4Jn_EklBRrML9vqrQ_60_1.jpeg",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/spro-bbz-1-swimbait-6-floating-blue-black-herring_zoom.jpeg",
    "https://cdn.shopify.com/s/files/1/0326/6501/products/gary-yamamoto-shad-shape-worm-green-pumpkin-watermelon-laminate_zoom.jpg"
]


def get_optimal_shopify_url(url, verify=0):

    # The magic only works on Shopify URL's
    if 'cdn.shopify.com' not in url:
        return url

    # Clean off the variant URL parameter
    new_url = re.sub(r'\?v=([0-9]*)', '', url)

    # Build a regex for finding built in dimension URL's
    regexp_dims = re.compile(r'_([0-9]*)x([0-9]*)\.')

    # If we find any, then substitute for the 1024x1024
    if regexp_dims.search(url):
        new_url = re.sub(r'_([0-9]*)x([0-9]*)\.', '_1024x1024.', new_url)

    # If we don't, add the 1024x1024 to the URL
    else:
        if ".jpg" in new_url:
            new_url = re.sub(r'.jpg', '_1024x1024.jpg', new_url)
        if ".jpeg" in new_url:
            new_url = re.sub(r'.jpeg', '_1024x1024.jpeg', new_url)
        if ".png" in new_url:
            new_url = re.sub(r'.png', '_1024x1024.png', new_url)

    # If we request to verify the URL, and it turns out the new URL doesn't work, just return the old one.

    if verify == 1:
        r = requests.get(new_url)
        if r.status_code != 200:
            return url

    return new_url


for url in urls:
    start_url = url
    print("URL: {}".format(url))
    new_url = get_optimal_shopify_url(url,1)
    print("URL: {}".format(new_url))
    print("")
