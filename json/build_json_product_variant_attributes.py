import json
import csv
import pprint

write_product_variant_attributes_json = True
if write_product_variant_attributes_json:


    pvav_json = {"products": []}
    with open("work/product_variant_attribute_values.csv", "r") as pvr:
        reader = csv.reader(pvr)
        pvav_list = list(reader)

        i = 0
        for pvav in pvav_list:

            if i == 0:
                i += 1
                continue
            else:
                i += 1

            product_found = False



            for product in pvav_json["products"]:
                if product["prod_id"] == pvav[2]:
                    print("Matched Prod_id")
                    product_found = True

                    variant_found = False
                    for v in product["variants"]:
                        if v["sku"] == pvav[11]:
                            variant_found = True

                            attribute = [{"id": pvav[3], "name": pvav[6], "value": pvav[9]}]
                            v["attributes"].append(attribute)
                            break

                    if variant_found == False:
                        attribute = [{"id": pvav[3], "name": pvav[6], "value": pvav[9]}]
                        variant = {"sku": pvav[11], "attributes": attribute}
                        product["variants"].append(variant)
                    break


            if product_found == False:

                attribute = [{"id": pvav[3], "name": pvav[6], "value": pvav[9]}]

                variant = [{"sku": pvav[11], "attributes": attribute}]

                pvav_json["products"].append({"id": pvav[0], "name": pvav[1], "prod_id": pvav[2], "variants": variant}) #, ""values": [{"id": pvav[2], "name": pvav[3]}]})


    print(pvav_json)
    pprint.pprint(pvav_json, depth=9, indent=5)

    # # Write attributes_json to a file attributes.json
    # with open("work/attribute_values.json", "w") as afw:
    #     afw.write(json.dumps(attribute_values_json))
