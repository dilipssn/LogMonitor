import json


def pretty_print(o, indent=1):
    pretty_data = json.dumps(o, indent=indent)  # accepts python list/dict and returns formatted string
    print(pretty_data)
