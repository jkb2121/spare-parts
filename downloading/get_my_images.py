import requests
import urllib.parse
import os
import time

# Data Set with all sorts of info, including the URL to scrape.
dataset = {
"rows":[
    {"prod_id": 4518, "sku": "CEPF38-01", "brand": "Z Man", "variant_detail": "Black/Blue", "handle": "z-man-crosseyez-power-finesse-jig-3-8-oz", "src": "https://i.ebayimg.com/images/g/kPMAAOSwtDdaX~7F/s-l1600.jpg"},
    {"prod_id": 4518, "sku": "CEPF38-02", "brand": "Z Man", "variant_detail": "Green Pumpkin", "handle": "z-man-crosseyez-power-finesse-jig-3-8-oz", "src": "https://i.ebayimg.com/images/g/rxgAAOSwhiZaX~7T/s-l1600.jpg"},
    {"prod_id": 4518, "sku": "CEPF38-03", "brand": "Z Man", "variant_detail": "Moccasin Craw", "handle": "z-man-crosseyez-power-finesse-jig-3-8-oz", "src": "https://i.ebayimg.com/images/g/8IEAAOSw-RFaX~7W/s-l1600.jpg"},
    {"prod_id": 4518, "sku": "CEPF38-04", "brand": "Z Man", "variant_detail": "Candy Craw", "handle": "z-man-crosseyez-power-finesse-jig-3-8-oz", "src": "https://i.ebayimg.com/images/g/fBEAAOSwp7FaX~7Q/s-l1600.jpg"},
    {"prod_id": 4518, "sku": "CEPF38-05", "brand": "Z Man", "variant_detail": "Pond Scum", "handle": "z-man-crosseyez-power-finesse-jig-3-8-oz", "src": "https://i.ebayimg.com/images/g/qjMAAOSwXsFaX~7m/s-l1600.jpg"},
    {"prod_id": 4518, "sku": "CEPF38-06", "brand": "Z Man", "variant_detail": "PB&J", "handle": "z-man-crosseyez-power-finesse-jig-3-8-oz", "src": "https://i.ebayimg.com/images/g/bikAAOSwM~taX~7h/s-l1600.jpg"},
    {"prod_id": 4518, "sku": "CEPF38-07", "brand": "Z Man", "variant_detail": "Natural Craw", "handle": "z-man-crosseyez-power-finesse-jig-3-8-oz", "src": "https://i.ebayimg.com/images/g/qYIAAOSweLBaX~7b/s-l1600.jpg"},
    {"prod_id": 4518, "sku": "CEPF38-08", "brand": "Z Man", "variant_detail": "Bruised Green Pumpkin", "handle": "z-man-crosseyez-power-finesse-jig-3-8-oz", "src": "https://i.ebayimg.com/images/g/GV0AAOSwZrhaX~7L/s-l1600.jpg"},
    {"prod_id": 4291, "sku": "Z015019", "brand": "Zoom", "variant_detail": "Watermelon Seed", "handle": "zoom-fluke-4-inch-10-pack", "src": "https://i.ebayimg.com/images/g/jIgAAOSwFyhaJaC9/s-l1600.jpg"},
    {"prod_id": 4291, "sku": "Z015045", "brand": "Zoom", "variant_detail": "White Pearl", "handle": "zoom-fluke-4-inch-10-pack", "src": "https://i.ebayimg.com/images/g/eboAAOSw3ZtaJaC1/s-l1600.jpg"},
    {"prod_id": 4291, "sku": "Z015091", "brand": "Zoom", "variant_detail": "Albino", "handle": "zoom-fluke-4-inch-10-pack", "src": "https://i.ebayimg.com/images/g/tSsAAOSwoYhaJaDB/s-l1600.jpg"},
    {"prod_id": 4291, "sku": "Z015109", "brand": "Zoom", "variant_detail": "Smokin Shad", "handle": "zoom-fluke-4-inch-10-pack", "src": "https://i.ebayimg.com/images/g/Gy0AAOSwc2FaJaC4/s-l1600.jpg"},
    {"prod_id": 4291, "sku": "Z015115", "brand": "Zoom", "variant_detail": "Baby Bass", "handle": "zoom-fluke-4-inch-10-pack", "src": "https://i.ebayimg.com/images/g/73MAAOSwJtdaJaCx/s-l1600.jpg"},
    {"prod_id": 4291, "sku": "Z015185", "brand": "Zoom", "variant_detail": "White Ice", "handle": "zoom-fluke-4-inch-10-pack", "src": "https://i.ebayimg.com/images/g/43UAAOSwVtZaJaDF/s-l1600.jpg"},
    {"prod_id": 4291, "sku": "Z015364", "brand": "Zoom", "variant_detail": "Lavender Shad", "handle": "zoom-fluke-4-inch-10-pack", "src": "https://i.ebayimg.com/images/g/yAoAAOSwOA1aJaEb/s-l1600.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-315", "brand": "Z Man", "variant_detail": "Blueback Herring", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/blue_back_herring_8ffc290a-9e54-4e35-971a-130968e1b383.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-311", "brand": "Z Man", "variant_detail": "Breaking Bream", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_311_Breaking_Bream_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-268", "brand": "Z Man", "variant_detail": "California Craw", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_268_California_Craw_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-60", "brand": "Z Man", "variant_detail": "Electric Chicken", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_60_Electric_Chicken_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-267", "brand": "Z Man", "variant_detail": "Houdini", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_267_Houdini_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-261", "brand": "Z Man", "variant_detail": "New Penny", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_261_New_Penny_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-263", "brand": "Z Man", "variant_detail": "Opening Night", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_263_Opening_Night_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-84", "brand": "Z Man", "variant_detail": "Pearl", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_84_Pearl_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-266", "brand": "Z Man", "variant_detail": "Redbone", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_266_Redbone_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-57", "brand": "Z Man", "variant_detail": "Smoky Shad", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_57_Smoky_Shad_horizontal.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-320", "brand": "Z Man", "variant_detail": "The Deal", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/the_deal_6e2b4a6a-7b0b-40df-9ebe-8dfea5b2d208.jpg"},
    {"prod_id": 3410, "sku": "GKICKERZ-92", "brand": "Z Man", "variant_detail": "Watermelon Candy", "handle": "z-man-grass-kickerz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_grass_kickerz_92_Watermelon_Candy_horizontal.jpg"},
    {"prod_id": 3409, "sku": "SCRB-231", "brand": "Z Man", "variant_detail": "Glow", "handle": "z-man-scented-crabz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_scented_crabz_231_Glow.jpg"},
    {"prod_id": 3409, "sku": "SCRB-31", "brand": "Z Man", "variant_detail": "Mud", "handle": "z-man-scented-crabz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_scented_crabz_31_Mud.jpg"},
    {"prod_id": 3409, "sku": "SCRB-27", "brand": "Z Man", "variant_detail": "Pearl Blue Glimmer", "handle": "z-man-scented-crabz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_scented_crabz_27_Blue_Glimmer.jpg"},
    {"prod_id": 3409, "sku": "SCRB-230", "brand": "Z Man", "variant_detail": "Rootbeer Gold", "handle": "z-man-scented-crabz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_scented_crabz_230_Rootbeer_Gold.jpg"},
    {"prod_id": 3409, "sku": "SCRB-18", "brand": "Z Man", "variant_detail": "Watermelon Red", "handle": "z-man-scented-crabz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z_man_scented_crabz_18_Watermelon_Red.jpg"},
    {"prod_id": 3242, "sku": "POPSHAD5-259", "brand": "Z Man", "variant_detail": "Bad Shad", "handle": "z-man-pop-shadz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z-man-pop-shadz-bad-shad.jpg"},
    {"prod_id": 3242, "sku": "POPSHAD5-311", "brand": "Z Man", "variant_detail": "Breaking Bream", "handle": "z-man-pop-shadz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z-man-pop-shadz-breaking-bream.jpg"},
    {"prod_id": 3242, "sku": "POPSHAD5-267", "brand": "Z Man", "variant_detail": "Houdini", "handle": "z-man-pop-shadz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z-man-pop-shadz-houdini.jpg"},
    {"prod_id": 3242, "sku": "POPSHAD5-281", "brand": "Z Man", "variant_detail": "Mud Minnow", "handle": "z-man-pop-shadz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z-man-pop-shadz-mud-minnow.jpg"},
    {"prod_id": 3242, "sku": "POPSHAD5-84", "brand": "Z Man", "variant_detail": "Pearl", "handle": "z-man-pop-shadz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z-man-pop-shadz-pearl.jpg"},
    {"prod_id": 3242, "sku": "POPSHAD5-266", "brand": "Z Man", "variant_detail": "Redbone", "handle": "z-man-pop-shadz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z-man-pop-shadz-redbone.jpg"},
    {"prod_id": 3242, "sku": "POPSHAD5-57", "brand": "Z Man", "variant_detail": "Smoky Shad", "handle": "z-man-pop-shadz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z-man-pop-shadz-smokey-shad.jpg"},
    {"prod_id": 3242, "sku": "POPSHAD5-17", "brand": "Z Man", "variant_detail": "Watermelon Chartreuse", "handle": "z-man-pop-shadz", "src": "https://cdn.shopify.com/s/files/1/0326/6501/products/z-man-pop-shadz-watermelon-chartreuse.jpg"}
]
}


# String with desired image URL, so when I move to AWS in this location, the url would work.
def make_image_url_string(prod_id, sku, handle, brand, variant_detail, src):
    return "{}/{}/{}".format(
        "http://www.awsplaceholder.com",
        make_image_disk_directory_string(prod_id, handle, brand),
        make_image_filename_string(prod_id, sku, handle, brand, variant_detail, src)
    )


# String with the path to the image directory on disk
def make_image_disk_directory_string(prod_id, handle, brand):
    bpath = urllib.parse.quote_plus(brand).lower()

    return "{}/{}_{}".format(bpath,prod_id, handle)


# String with the image filename
def make_image_filename_string(prod_id, sku, handle, brand, variant_detail, src):
    bpath = urllib.parse.quote_plus(brand).lower()
    vdpath = urllib.parse.quote_plus(variant_detail).lower()
    skupath = urllib.parse.quote_plus(sku).upper()

    if src.endswith(".png"):
        ext = "png"
    elif src.endswith(".jpg"):
        ext = "jpg"
    elif src.endswith(".gif"):
        ext = "gif"
    else:
        ext = "jpg"

    mfilename = "{}_{}_{}_{}_{}.{}".format(bpath, prod_id, skupath, handle, vdpath, ext)

    return mfilename


print("Get My Images!")

for row in dataset["rows"]:
    print("Row: {}".format(row))

    src_url = row["src"]

    mdir = make_image_disk_directory_string(row["prod_id"], row["handle"], row["brand"])
    filename = make_image_filename_string(row["prod_id"], row["sku"], row["handle"], row["brand"], row["variant_detail"], row["src"])
    image_url = make_image_url_string(row["prod_id"], row["sku"], row["handle"], row["brand"], row["variant_detail"], row["src"])

    print("Directory: {}".format(mdir))
    print("Filename: {}".format(filename))
    print("Image URL: {}".format(image_url))

    # Does the directory path exist?
    working_path = "work"
    # print("Working Path Exists?  {}".format(os.path.isdir(working_path)))

    image_folder = "{}/{}".format(working_path, mdir)

    if not os.path.isdir(image_folder):
        print("Creating Image Folder Path")

        makepath = image_folder.split("/")

        dt = ""
        delim = ""
        for d in makepath:
            dt = "{}{}{}".format(dt, delim, d)
            delim = "/"
            if not os.path.isdir(dt):
                os.mkdir(dt)
    else:
        print("Image Folder Path Exists")


    # Set the headers so it looks like a legit customer browser.
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    r = requests.get(src_url, headers=headers, stream=True)
    write_image_path = "{}/{}".format(image_folder, filename)

    # for each chunk of the image, write it to the file specified
    with open(write_image_path, 'wb') as fd:
        for chunk in r.iter_content(2000):
            fd.write(chunk)

    print("\n--------------------------------")

    # Sleep for a moment so we don't agitate any of the target CDN hosts
    time.sleep(1)

print("Normal End of Program")