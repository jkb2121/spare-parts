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
                    product_found = True

                    variant_found = False
                    for v in product["variants"]:
                        if v["sku"] == pvav[11]:
                            variant_found = True

                            attribute = {"id": pvav[3], "name": pvav[6], "value": pvav[9]}
                            v["attributes"].append(attribute)
                            break

                    if variant_found == False:
                        attribute = [{"id": pvav[3], "name": pvav[6], "value": pvav[9]}]
                        variant = {"sku": pvav[11], "type": "product", "attributes": attribute}
                        product["variants"].append(variant)

                        if not {"id": pvav[3], "name": pvav[6]} in product["attribute_ids"]:
                            product["attribute_ids"].append({"id": pvav[3], "name": pvav[6]})
                        if not {"value": pvav[9]} in product["attribute_value_ids"]:
                            product["attribute_value_ids"].append({"value": pvav[9]})
                    break


            if product_found == False:

                attribute_ids = [{"id": pvav[3], "name": pvav[6]}]
                attribute_value_ids = [{"value": pvav[9]}]

                attribute = [{"id": pvav[3], "name": pvav[6], "value": pvav[9]}]

                variant = [{"sku": pvav[11], "attributes": attribute}]

                pvav_json["products"].append({"id": pvav[0], "name": pvav[1], "prod_id": pvav[2], "type": "product",
                                              "variants": variant, "attribute_ids": attribute_ids,
                                              "attribute_value_ids": attribute_value_ids})


    print(pvav_json)
    pprint.pprint(pvav_json, depth=9, indent=5)

    # Write attributes_json to a file attributes.json
    with open("work/product_variant_attributes.json", "w") as afw:
        afw.write(json.dumps(pvav_json))
