from bs4 import BeautifulSoup
import requests

import csv
from collections import OrderedDict

#
# Run this one Third!
#
# Basically, what we're doing in this file is building a .csv file with the resulting data from my scrape.
# I'm using the OrderedDict because I want my file to be a certain order of columns and blanks to be permitted.
#

scrape_results_file = open("scrape_results_file.csv", 'w', newline='')

ordered_fieldnames = OrderedDict([
    ('itemOffered', None),
    ('price', None),
    ("sku", None),
    ("gtin13", None),
    ("priceCurrency", None),
    ('url', None)
])

ss_writer = csv.DictWriter(scrape_results_file, delimiter=',', quotechar='"',
                           fieldnames=ordered_fieldnames, quoting=csv.QUOTE_MINIMAL)
ss_writer.writeheader()

#
# I was lazy and copied this data from the output of get_descpages_from_catpages.py after deduping and formatting
#
domain = "http://www.redacted.com"
urls = [
'/River2Sea_Goon_Crankbaits/descpage-R2SGCB.html',
'/River2Sea_Ish_Monroe_Biggie_Square_Bill_Crankbaits/descpage-R2SBSB.html',
'/River2sea_Larry_Dahlberg_Clackin_Crayfish/descpage-R2SCCR.html',
'/River2Sea_Ruckus_Lipless_Crankbaits/descpage-R2SRLL.html',
'/River2Sea_Bubble_Popper/descpage-RSBP.html',
'/River2Sea_Bubble_Walker/descpage-R2SBUB.html',
'/River2Sea_Chris_Lane_Big_Mistake/descpage-R2SCLBM.html',
'/River2Sea_Chris_Lane_Lane_Changer/descpage-R2SLC.html',
'/River2Sea_Chris_Lane_Top_Notch/descpage-R2STN.html',
'/River2Sea_Ish_Monroe_Phat_Matt_Daddy_Frog/descpage-R2SPMDF.html',
'/River2Sea_Phat_Frog_Kit/descpage-R2SPFK.html',
'/River2Sea_Pro_Tuned_Rover/descpage-R2SPTR.html',
'/River2Sea_Whopper_Plopper/descpage-R2SWP13.html',
'/River2Sea_Whopper_Plopper_Silent/descpage-R2SWPS.html',
'/River2Sea_Rig_Walker_Swimbaits/descpage-R2SRW.html',
'/River2Sea_S-Waver/descpage-R2SW.html',
'/River2Sea_Ish_Bling_Colorado_Indiana_Spinnerbait/descpage-R2SBCI.html',
'/River2Sea_Ish_Monroe_Bling_Double_Willow_Spinnerbait/descpage-R2SBSBT.html',
'/River2Sea_Double_Plopper_Buzzbaits/descpage-R2SDP.html',
'/River2Sea_Bully_Wa_2_Frog/descpage-RBW2.html',
'/River2Sea_Tommy_Biffle_Spittin_Wa_Frog/descpage-RSPW.html',
'/River2Sea_John_Murray_Papa_Mur_Jigs/descpage-RSPMJ.html',
'/River2Sea_Tommy_Biffle_Junkyard_Jigs/descpage-R2SBJJ.html',
'/River2Sea_Ish_Monroe_New_Jack_Flippin_Hooks_4_pk/descpage-R2SNJFH.html',
'/River2Sea_Bumbershoot_Umbrella_Rig/descpage-R2SBS.html',
'/River2Sea_Peter_Thliveros_PT_Hook_4pk/descpage-R2SPTH.html',
'/River2Sea_Tungsten_Trash_Bomb_Weights_1pk/descpage-RSTB.html',
'/River2Sea_Short_Sleeve_Tee_Shirt/descpage-R2SSST.html',
'/River2Sea_Whopper_Plopper_T-Shirt/descpage-R2SWPTS.html',
'/River2Sea_Hooded_Sweatshirt/descpage-R2SH.html',
'/River2Sea_Goon_Crankbaits/descpage-R2SGCB.html',
'/Roboworm_Alive_Shad/descpage-RBWLS.html',
'/Roboworm_Curly_Tail_Worm_45/descpage-RW45CT.html',
'/Roboworm_Fat_Straight_Tail_Worms/descpage-RFST.html',
'/Roboworm_FX_Sculpins/descpage-RWFX4S.html',
'/Roboworm_FX_Straight_Tail_Worms/descpage-RWFX4.html',
'/Roboworm_Ned_Worms/descpage-ROBONED.html',
'/Roboworm_Straight_Tail_Worms/descpage-RW45ST.html',
'/Roboworm_Textured_Curl_Tail_Worms_55_/descpage-RCLW.html',
'/Roboworm_Zipper_Grub_35_/descpage-RW35ZG.html',
'/Roboworm_Zipper_Worms/descpage-RW5Z.html',
'/Roboworm_EZ_Shad_Swimbait_5_3pk/descpage-REZS.html',
'/Roboworm_Robo_Minnow_Swimbaits_5pk/descpage-RWRM.html',
'/Roboworm_Rebarb_Hooks/descpage-RWRBH.html',
'/Keitech_Swing_Impact_FAT_Swimbait/descpage-KSIF.html']

#
# So for each of the URL's above, we hit the page, look for all of the instances of <td class="qty_cell"... where the
# data is embedded in some Schema tags...
#

for xurl in urls:
    url = "{}{}".format(domain, xurl)
    r = requests.get(url).text

    soup = BeautifulSoup(r, 'html.parser')

    cells = soup.findAll("td", {"class": "qty_cell"})
    for cell in cells:
        # print("Cell: {}".format(cell))
        print("---------------------------------------")

        #
        # We'll store the data once we find it in this dict
        #

        scrape_data = {
            'itemOffered': '',
            'price': '',
            'sku': '',
            'gtin13': '',
            'priceCurrency': '',
            'url': url
        }

        for input in cell.children:

            if input.name is None:
                continue

            if input.name == 'input':
                continue

            #
            # The good stuff is in these meta tags...
            #

            if input.name == 'meta':
                print("Prop: {}, Content: {}".format(input["itemprop"], input["content"]))

                #
                # Add it to the dict
                #

                scrape_data[input["itemprop"]] = input["content"]

        #
        # Write the dict containing the data to the .csv
        #

        # print("Scrape_Data: {}".format(scrape_data))
        ss_writer.writerow(scrape_data)

scrape_results_file.close()

