import json
import csv
import pprint

write_attributes_json = True
if write_attributes_json:
    # Read attributes.csv into an attributes_json array.
    attributes_json = {"attributes": []}
    with open("work/attributes.csv", "r") as afr:
        reader = csv.reader(afr)
        attribute_list = list(reader)

        i = 0
        for al in attribute_list:

            if i == 0:
                i += 1
                continue
            else:
                i += 1

            attributes_json["attributes"].append({"id": al[0], "name": al[1]})

    print(attributes_json)
    pprint.pprint(attributes_json)

    # Write attributes_json to a file attributes.json
    with open("work/attributes.json", "w") as afw:
        afw.write(json.dumps(attributes_json))

write_attribute_values_json = True
if write_attribute_values_json:
    # Read attributes.csv into an attributes_json array.
    attribute_values_json = {"attributes": []}
    with open("work/attribute_values.csv", "r") as afr:
        reader = csv.reader(afr)
        attribute_values_list = list(reader)

        i = 0
        for avl in attribute_values_list:
            if i == 0:
                i += 1
                continue
            else:
                i += 1

            found = False
            for attribute in attribute_values_json["attributes"]:
                try:
                    if attribute["name"] == avl[1]:
                        found = True

                        attribute["values"].append({"id": avl[2], "name": avl[3]})
                        break
                except AttributeError:
                    found = False
                    break


            if found == False:
                attribute_values_json["attributes"].append({"id": avl[0], "name": avl[1], "values": [{"id": avl[2], "name": avl[3]}]})


    print(attribute_values_json)
    pprint.pprint(attribute_values_json)

    # Write attributes_json to a file attributes.json
    with open("work/attribute_values.json", "w") as afw:
        afw.write(json.dumps(attribute_values_json))
