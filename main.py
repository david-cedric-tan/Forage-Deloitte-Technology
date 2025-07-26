
import json
from datetime import datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)

with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)


def convertFromFormat1 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    result = {}
    result["deviceID"] = jsonObject["deviceID"]
    result["deviceType"] = jsonObject["deviceType"]
    result["timestamp"] = jsonObject["timestamp"]

    loc_categories = ["country", "city", "area", "factory", "section"]
    data_list = jsonObject["location"].split("/")

    location = {}
    for i in range(min(len(data_list), len(loc_categories))):
        location[loc_categories[i]] = data_list[i]
    result["location"] = location

    data_cat= {
        "operationStatus": "status",
        "temp":            "temperature"
    }
    result["data"] = {
        new_cat: jsonObject[old_cat]
        for old_cat, new_cat in data_cat.items()
    }
    return result

def convertFromFormat2 (jsonObject):

    # IMPLEMENT: Conversion From Type 1
    result = {}
    result["deviceID"] = jsonObject["device"]["id"]
    result["deviceType"] = jsonObject["device"]["type"]
    timestamp = jsonObject["timestamp"] 
    iso_date = datetime.fromisoformat(timestamp).timestamp() 
    result["timestamp"] = int(iso_date*1000)

    loc_categories = ["country", "city", "area", "factory", "section"]
    result["location"] = {cat: jsonObject[cat] for cat in loc_categories}
    
    data_cat = ["status","temperature"]
    result["data"] = {cat: jsonObject["data"][cat] for cat in data_cat}
    return result

def main (jsonObject):

    result = {}
    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


if __name__ == '__main__':
    result = main(jsonData2)

    print(json.dumps(result, indent=2))