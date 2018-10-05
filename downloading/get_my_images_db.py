import requests
import urllib.parse
import os
import time
import sys
import yaml

from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker, mapper


if len(sys.argv) != 2:
    print("Usage:  get_my_images_db.py <config.yaml>")
    exit(1)

try:
    print("Using Configuration File: " + sys.argv[1])
    with open(sys.argv[1], 'r') as f:
        yml = yaml.load(f)

        db_driver = yml['peck_database_info']['db_driver']
        db_username = yml['peck_database_info']['db_username']
        db_password = yml['peck_database_info']['db_password']
        db_server = yml['peck_database_info']['db_server']
        db_dbname = yml['peck_database_info']['db_dbname']

except IOError:
    print("Error Opening Config File: " + sys.argv[1])
    exit(1)

engine = create_engine('{}://{}:{}@{}/{}'.format(db_driver, db_username, db_password, db_server, db_dbname), echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# String with desired image URL, so when I move to AWS in this location, the url would work.
def make_image_url_string(prod_id, sku, handle, brand, variant_detail, src):
    return "{}/{}/{}".format(
        "http://www.awsplaceholder.com",
        make_image_disk_directory_string(prod_id, handle, brand),
        make_image_filename_string(prod_id, sku, handle, brand, variant_detail, src)
    )


# String with the path to the image directory on disk
def make_image_disk_directory_string(brand, handle):
    bpath = urllib.parse.quote_plus(brand).lower()

    return "{}/{}".format(bpath, handle)


# String with the image filename
def make_image_filename_string(brand, handle, variant_detail, src):
    src = src.lower()
    bpath = urllib.parse.quote_plus(brand).lower()
    vdpath = urllib.parse.quote_plus(variant_detail).lower()

    if src.endswith(".png"):
        ext = "png"
    elif src.endswith(".jpg"):
        ext = "jpg"
    elif src.endswith(".gif"):
        ext = "gif"
    else:
        ext = "jpg"

    mfilename = "{}.{}".format(vdpath, ext)

    return mfilename


# Data Set with all sorts of info, including the URL to scrape.
with engine.connect() as conn:
    sql = text('''
    SELECT 
        sh.shopify_handle AS handle
        ,sd.Variant_Detail AS variant_detail
        ,pd.brand
        ,sd.src
        ,sd.Product_ID
        ,sd.sku
    FROM 
        product_variant_map pvm
        INNER JOIN product_data pd ON pvm.Product_ID=pd.prod_id
        INNER JOIN sku_details sd ON pvm.Product_ID=sd.Product_ID AND pvm.SKU=sd.SKU
        INNER JOIN shopify_handle sh ON sh.prod_id=pvm.Product_ID
    WHERE 
        1=1
        AND (pd.brand LIKE 'seaguar%' OR pd.brand LIKE 'rapala%' OR pd.brand LIKE 'lucky craft%' OR pd.brand LIKE 'megabass%')
        AND sh.site='discount-tackle-dotcom'
        AND sd.src != 'novariant'
        
    
    ;
        
        ''')


    output = open("output.csv", "w");

    rows = conn.execute(sql, {})
    for row in rows:
        print("Row: {}".format(row))

        src_url = row[3]

        mdir = make_image_disk_directory_string(row["brand"], row["handle"])
        filename = make_image_filename_string(row["brand"], row["handle"], row["variant_detail"], row["src"])
        # image_url = make_image_url_string(row["prod_id"], row["sku"], row["handle"], row["brand"], row["variant_detail"], row["src"])

        print("Directory: {}".format(mdir))
        print("Filename: {}".format(filename))
        # print("Image URL: {}".format(image_url))

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

        write_image_path = "{}/{}".format(image_folder, filename)

        url = "https://mcproductimages.s3-us-west-2.amazonaws.com/{}/{}".format(urllib.parse.quote(mdir),
                                                                                urllib.parse.quote(filename))
        output.write("{}, {}, {}, {}\n".format(row["Product_ID"], row["sku"], row["src"], url))

        if os.path.isfile(write_image_path):
            continue

        # Set the headers so it looks like a legit customer browser.
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
        r = requests.get(src_url, headers=headers, stream=True)


        # for each chunk of the image, write it to the file specified
        with open(write_image_path, 'wb') as fd:
            for chunk in r.iter_content(2000):
                fd.write(chunk)

        print("\n--------------------------------")

        # Sleep for a moment so we don't agitate any of the target CDN hosts
        time.sleep(1)

    output.close()


print("Normal End of Program")