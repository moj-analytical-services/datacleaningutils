import json
def read_json(filename) :
    with open(filename) as json_data:
        data = json.load(json_data)
    return data